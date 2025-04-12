import sys, os
from PyQt5.QtWidgets import *
##Libraries used##: QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QLineEdit, QSizePolicy, QCheckBox, QMessageBox # Added imports
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

# --- Imports Added ---
import sqlite3
# --- End Imports Added ---

class MainWindow(QMainWindow): # Renaming to ManageCardDialog might be clearer
    def __init__(self, card_id, parent=None): # Accept card_id and parent (main window)
        super().__init__(parent) # Pass parent to superclass
        self.card_id = card_id
        # self.parent_window = parent # Store parent if needed for more interaction

        self.setWindowTitle("Manage Card")
        self.setFixedSize(250, 250)
         # Ensure placeholder.jpg is in the same directory or provide a full path
        icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "placeholder.jpg")
        if os.path.exists(icon_path):
             self.setWindowIcon(QIcon(icon_path))
        else:
             print(f"Warning: Icon file not found at {icon_path}")


        # --- Fetch initial lock state ---
        self.is_locked = self.get_lock_status()
        # ---

        # Declare UI elements
        self.lockBtn = QPushButton("Lock Card" if not self.is_locked else "Unlock Card", self)
        self.unlockCkBx = QCheckBox("Enable Delete/Lock", self) # Changed text slightly
        self.deleteBtn = QPushButton("Delete Card", self)
        self.okBtn = QPushButton("Close", self) # Changed text to "Close"
        self.cleanBtn = QPushButton("Clean History", self)

        self.initUi()

        # Initial lock state for buttons controlled by checkbox
        self.lockBtn.setEnabled(False)
        self.deleteBtn.setEnabled(False)

        # Connections
        self.unlockCkBx.stateChanged.connect(self.toggle_lock_delete)
        self.lockBtn.clicked.connect(self.toggle_lock_card) # Changed connect function
        self.deleteBtn.clicked.connect(self.delete_card)
        self.cleanBtn.clicked.connect(self.clean_history)
        self.okBtn.clicked.connect(self.close) # Close this dialog

    def get_lock_status(self):
        """Gets the current lock status from the database."""
        conn = None
        is_locked = False
        try:
            db_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bank.db")
            if not os.path.exists(db_file): return False # Assume unlocked if DB error
            conn = sqlite3.connect(db_file)
            cursor = conn.cursor()
            cursor.execute("SELECT isLocked FROM cards WHERE id = ?", (self.card_id,))
            result = cursor.fetchone()
            if result:
                is_locked = bool(result[0])
        except sqlite3.Error as e:
            print(f"Database error getting lock status: {e}")
        finally:
            if conn:
                conn.close()
        return is_locked

    def initUi(self):
        # Using provided setGeometry - consider layouts
        self.lockBtn.setGeometry(20, 20, 141, 23) # Moved Lock button up
        self.cleanBtn.setGeometry(20, 60, 141, 23)
        self.deleteBtn.setGeometry(20, 100, 141, 23) # Moved Delete button down
        self.unlockCkBx.setGeometry(20, 140, 180, 23) # Positioned checkbox
        self.okBtn.setGeometry(int((250-75)/2), 200, 75, 23) # Centered OK button


    def toggle_lock_delete(self, state):
        """Enables/disables Lock and Delete buttons based on checkbox."""
        enabled = state == Qt.Checked
        self.lockBtn.setEnabled(enabled)
        self.deleteBtn.setEnabled(enabled)

    def toggle_lock_card(self):
        """Toggles the lock status of the card in the database."""
        new_lock_status = not self.is_locked # Determine the new state
        new_lock_value = 1 if new_lock_status else 0 # 1 for locked, 0 for unlocked
        action_text = "lock" if new_lock_status else "unlock"

        conn = None
        try:
            db_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bank.db")
            if not os.path.exists(db_file):
                 QMessageBox.warning(self, "Error", "Database file not found.")
                 return
            conn = sqlite3.connect(db_file)
            cursor = conn.cursor()

            cursor.execute("UPDATE cards SET isLocked = ? WHERE id = ?", (new_lock_value, self.card_id))
            conn.commit()

            # --- Update internal state and UI ---
            self.is_locked = new_lock_status
            self.lockBtn.setText("Unlock Card" if self.is_locked else "Lock Card")
            QMessageBox.information(self, "Success", f"Card has been {action_text}ed.")

            # --- Update parent window (main.py) ---
            #Need to log in again in order to see the update on the main.py window (for now...)

            if self.parent() and hasattr(self.parent(), 'load_card_details'):
                 self.parent().load_card_details() # Reload details in main window to update lock status and button states there

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"Failed to {action_text} card: {e}")
            print(f"Database error toggling lock status: {e}")
            if conn: conn.rollback()
        except Exception as e:
             QMessageBox.critical(self, "Error", f"An unexpected error occurred: {e}")
             print(f"An error occurred toggling lock status: {e}")
             if conn: conn.rollback()
        finally:
            if conn:
                conn.close()


    def clean_history(self):
        """Deletes all transactions for this card from the database."""
        reply = QMessageBox.question(self, "Confirm Clean History",
                                     "Are you sure you want to permanently delete all transaction history for this card?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            conn = None
            try:
                db_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bank.db")
                if not os.path.exists(db_file):
                     QMessageBox.warning(self, "Error", "Database file not found.")
                     return
                conn = sqlite3.connect(db_file)
                cursor = conn.cursor()

                cursor.execute("DELETE FROM transactions WHERE card_id = ?", (self.card_id,))
                conn.commit()

                QMessageBox.information(self, "History Cleared", "Transaction history has been cleared.")

                # --- Update parent window (main.py) ---
                if self.parent() and hasattr(self.parent(), 'load_transactions'):
                     self.parent().load_transactions() # Refresh transaction list in main window

            except sqlite3.Error as e:
                QMessageBox.critical(self, "Database Error", f"Failed to clear history: {e}")
                print(f"Database error cleaning history: {e}")
                if conn: conn.rollback()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"An unexpected error occurred: {e}")
                print(f"An error occurred cleaning history: {e}")
                if conn: conn.rollback()
            finally:
                if conn:
                    conn.close()


    def delete_card(self):
        """Deletes the card after checking balance and confirming."""
        conn = None
        try:
            db_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bank.db")
            if not os.path.exists(db_file):
                 QMessageBox.warning(self, "Error", "Database file not found.")
                 return

            conn = sqlite3.connect(db_file)
            cursor = conn.cursor()

            # --- Check Balance ---
            cursor.execute("SELECT balance, user_id FROM cards WHERE id = ?", (self.card_id,))
            result = cursor.fetchone()
            if not result:
                 QMessageBox.warning(self, "Error", "Card not found.")
                 return
            balance, user_id = result

            # --- Check for other cards (simplified logic) ---
            cursor.execute("SELECT COUNT(*) FROM cards WHERE user_id = ? AND id != ?", (user_id, self.card_id))
            other_cards_count = cursor.fetchone()[0]

            if balance > 0:
                if other_cards_count > 0:
                    choice = QMessageBox.question(
                        self,
                        "Transfer Funds?", # Simplified - just requires zeroing balance
                        f"This card has a balance of ${balance:,.2f}. You must zero the balance before deleting.\n(Simulating transfer to another account). Proceed?",
                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No
                    )
                    if choice == QMessageBox.Yes:
                        # Zero the balance in the database
                        cursor.execute("UPDATE cards SET balance = 0 WHERE id = ?", (self.card_id,))
                        # Add a transaction note (optional)
                        cursor.execute("""
                            INSERT INTO transactions (card_id, transaction_type, amount)
                            VALUES (?, ?, ?)
                            """, (self.card_id, 'transfer_out_delete', balance))
                        conn.commit() # Commit the balance change
                        balance = 0 # Update local balance variable
                        QMessageBox.information(self, "Balance Zeroed", "Balance set to zero. Ready for deletion.")
                    else:
                        QMessageBox.warning(self, "Cancelled", "Card deletion cancelled. Balance remains.")
                        return # Stop deletion process
                else:
                    # No other cards exist to "transfer" to
                    QMessageBox.critical(self, "Cannot Delete", f"Card has a balance of ${balance:,.2f} and no other account exists to transfer to. Please withdraw funds first.")
                    return # Stop deletion process

            # --- Confirmation ---
            confirm_reply = QMessageBox.question(self, "Confirm Deletion",
                                                 "Are you sure you want to permanently delete this card and its history?",
                                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if confirm_reply == QMessageBox.Yes:
                # --- Delete Card (ON DELETE CASCADE handles transactions) ---
                cursor.execute("DELETE FROM cards WHERE id = ?", (self.card_id,))
                conn.commit()

                QMessageBox.information(self, "Card Deleted", "Card has been successfully deleted.")

                # --- Close Windows ---
                if self.parent():
                    self.parent().close() # Close the main window
                self.close() # Close this manage dialog

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"Failed to delete card: {e}")
            print(f"Database error deleting card: {e}")
            if conn: conn.rollback()
        except Exception as e:
             QMessageBox.critical(self, "Error", f"An unexpected error occurred: {e}")
             print(f"An error occurred deleting card: {e}")
             if conn: conn.rollback()
        finally:
            if conn:
                conn.close()


def main():
    # This main function is primarily for testing this window in isolation
    app = QApplication(sys.argv)
    # Provide a dummy card_id and optionally a dummy parent for testing
    test_card_id = 1
    # Create a dummy parent if needed for testing interactions
    class DummyParent(QWidget):
         def load_card_details(self): print("DummyParent: load_card_details called")
         def load_transactions(self): print("DummyParent: load_transactions called")
         def close(self): print("DummyParent: close called"); super().close()

    # window = MainWindow(test_card_id, DummyParent()) # Use dummy parent
    window = MainWindow(test_card_id) # Or run without parent reference for basic UI check
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()