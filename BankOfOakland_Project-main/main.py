import sys, os
from PyQt5.QtWidgets import *
##Libraries used##: QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QLineEdit, QSizePolicy, QListWidget, QInputDialog, QMessageBox # Added needed imports
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt, QRect

# --- Imports Added ---
import sqlite3
import datetime
# --- End Imports Added ---

# --- Make sure manageCardBox.py is importable ---
from manageCardBox import MainWindow as ManageCardWindow
# --- End Import Check ---

class MainWindow(QMainWindow):
    def __init__(self, card_id): # Accept card_id from cardSelection
        super().__init__()
        self.card_id = card_id # Store the selected card's ID
        self.balance = 0.00 # Initialize balance, will be loaded
        self.is_locked = False # Initialize lock status

        self.setWindowTitle("Bank of Oakland: Account Details") # Dynamic title later?
        self.setFixedSize(830, 520) #(x, y, width, height)
         # Ensure placeholder.jpg is in the same directory or provide a full path
        icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "placeholder.jpg")
        if os.path.exists(icon_path):
             self.setWindowIcon(QIcon(icon_path))
        else:
             print(f"Warning: Icon file not found at {icon_path}")


        #DeclareValues
        self.balanceStaticLbl = QLabel("Balance:",self)
        self.balanceLbl = QLabel("$----.--", self) # Placeholder balance
        self.accountStaticLbl = QLabel("Account Number:",self)
        self.accountInfoLbl = QLabel("<Card Number> <Account Holder Name>", self) # Placeholder info
        self.transactionsList = QListWidget(self)
        self.transactionsStaticLbl = QLabel("Transactions:",self)
        self.depositBtn = QPushButton("Deposit", self)
        self.accountLbl = QLabel("XXXXXXXXX", self) # Placeholder account num
        self.routingLbl = QLabel("XXXXXXXXX", self) # Placeholder routing num
        self.routingStaticLbl = QLabel("Routing Number:", self)
        self.transferBtn = QPushButton("Transfer", self)
        self.manageCardBtn = QPushButton("Manage Card", self)
        self.withdrawBtn = QPushButton("Withdraw", self)

        self.initUi()
        self.load_card_details() # Load details after UI setup
        self.load_transactions() # Load transactions after UI setup
        self.update_button_states() # Set initial button states based on lock status

        # Connect buttons
        self.depositBtn.clicked.connect(self.handle_deposit)
        self.withdrawBtn.clicked.connect(self.handle_withdraw)
        self.transferBtn.clicked.connect(self.handle_transfer)
        self.manageCardBtn.clicked.connect(self.open_manage_card)

    def initUi(self):
        # Using provided setGeometry calls - consider layouts for better resizing
        self.balanceStaticLbl.setGeometry(QRect(40, 30, 181, 40))
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.balanceStaticLbl.setFont(font)

        self.balanceLbl.setGeometry(QRect(230, 30, 310, 40)) # Increased width for larger balances
        self.balanceLbl.setFont(font)
        self.balanceLbl.setAlignment(Qt.AlignLeft | Qt.AlignVCenter) # Align left

        self.accountStaticLbl.setGeometry(QRect(40, 430, 211, 41))
        font1 = QFont()
        font1.setPointSize(20)
        self.accountStaticLbl.setFont(font1)

        self.accountInfoLbl.setGeometry(QRect(40, 80, 461, 31))
        font2 = QFont()
        font2.setPointSize(15)
        font2.setItalic(False)
        self.accountInfoLbl.setFont(font2)

        self.transactionsList.setGeometry(QRect(510, 80, 270, 400))

        self.transactionsStaticLbl.setGeometry(QRect(510, 40, 121, 41))
        font3 = QFont()
        font3.setPointSize(15)
        self.transactionsStaticLbl.setFont(font3)

        self.depositBtn.setGeometry(QRect(40, 120, 331, 51))
        self.depositBtn.setFont(font3)

        self.accountLbl.setGeometry(QRect(260, 430, 200, 41)) # Increased width
        self.accountLbl.setFont(font1)

        self.routingStaticLbl.setGeometry(QRect(40, 470, 211, 41))
        self.routingStaticLbl.setFont(font1)

        self.routingLbl.setGeometry(QRect(260, 470, 200, 41)) # Increased width
        self.routingLbl.setFont(font1)

        self.withdrawBtn.setGeometry(QRect(40, 190, 331, 51))
        self.withdrawBtn.setFont(font3)

        self.transferBtn.setGeometry(QRect(40, 260, 331, 51))
        self.transferBtn.setFont(font3)

        self.manageCardBtn.setGeometry(QRect(40, 330, 331, 51))
        self.manageCardBtn.setFont(font3)


    def load_card_details(self):
        """Loads card details (balance, numbers, owner) from the database."""
        conn = None
        try:
            db_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bank.db")
            if not os.path.exists(db_file):
                 QMessageBox.warning(self, "Error", "Database file not found.")
                 return
            conn = sqlite3.connect(db_file)
            cursor = conn.cursor()

            # Fetch card details and user's name
            cursor.execute("""
                SELECT c.card_number, c.accountNum, c.routingNum, c.balance, u.firstname, u.lastname, c.isLocked
                FROM cards c
                JOIN users u ON c.user_id = u.id
                WHERE c.id = ?
            """, (self.card_id,))
            card_data = cursor.fetchone()

            if card_data:
                card_num, acc_num, rout_num, balance, first_name, last_name, is_locked = card_data
                self.balance = balance
                self.is_locked = bool(is_locked) # Convert 0/1 to False/True

                # Update UI elements
                self.accountInfoLbl.setText(f"Card: **** {card_num[-4:]}  Holder: {first_name} {last_name}")
                self.accountLbl.setText(str(acc_num))
                self.routingLbl.setText(str(rout_num))
                self.setWindowTitle(f"Bank of Oakland: Account **** {card_num[-4:]}") # Update window title
                self.update_balance_display()
                self.update_button_states() # Update buttons based on loaded lock status

            else:
                 QMessageBox.critical(self, "Error", "Could not load card details.")
                 self.close() # Close window if card details can't be found

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"Failed to load card details: {e}")
            print(f"Database error loading card details: {e}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An unexpected error occurred: {e}")
            print(f"An error occurred loading card details: {e}")
        finally:
            if conn:
                conn.close()

    def load_transactions(self):
        """Loads transaction history from the database."""
        self.transactionsList.clear() # Clear previous entries
        conn = None
        try:
            db_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bank.db")
            if not os.path.exists(db_file): return # Don't try if DB doesn't exist
            conn = sqlite3.connect(db_file)
            cursor = conn.cursor()

            # Fetch transactions, ordered by date descending
            cursor.execute("""
                SELECT transaction_type, amount, transaction_date
                FROM transactions
                WHERE card_id = ?
                ORDER BY transaction_date DESC
            """, (self.card_id,))
            transactions = cursor.fetchall()

            if transactions:
                for trans_type, amount, timestamp in transactions:
                     # Format timestamp nicely
                     # dt_object = datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
                     # formatted_time = dt_object.strftime('%Y-%m-%d %H:%M') # Example format
                     # For simplicity, just use the raw timestamp for now
                     formatted_time = timestamp.split('.')[0] # Remove microseconds if present
                     sign = "+" if trans_type.lower() == 'deposit' else "-"
                     item_text = f"{formatted_time} | {trans_type.capitalize()} | {sign}${abs(amount):,.2f}"
                     self.transactionsList.addItem(item_text)
            else:
                 self.transactionsList.addItem("No transactions found.")

        except sqlite3.Error as e:
            print(f"Database error loading transactions: {e}")
            self.transactionsList.addItem("Error loading transactions.")
        except Exception as e:
            print(f"An error occurred loading transactions: {e}")
        finally:
            if conn:
                conn.close()

    def update_balance_display(self):
        """Updates the balance label with current formatted balance."""
        self.balanceLbl.setText(f"${self.balance:,.2f}")

    def update_button_states(self):
        """Enables/disables buttons based on card lock status."""
        enabled = not self.is_locked
        self.depositBtn.setEnabled(enabled)
        self.withdrawBtn.setEnabled(enabled)
        self.transferBtn.setEnabled(enabled)
        if self.is_locked:
             self.balanceStaticLbl.setText("Balance (Locked):")
        else:
             self.balanceStaticLbl.setText("Balance:")


    def perform_transaction(self, transaction_type, amount):
        """Helper function to update balance and record transaction in DB."""
        conn = None
        success = False
        try:
            db_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bank.db")
            if not os.path.exists(db_file):
                 QMessageBox.warning(self, "Error", "Database file not found.")
                 return False

            conn = sqlite3.connect(db_file)
            cursor = conn.cursor()

            # Determine balance change
            balance_change = 0
            if transaction_type == 'deposit':
                balance_change = amount
            elif transaction_type in ['withdrawal', 'transfer']:
                balance_change = -amount
            else:
                 print(f"Unknown transaction type: {transaction_type}")
                 return False # Should not happen

            # --- Update Balance in DB ---
            cursor.execute("UPDATE cards SET balance = balance + ? WHERE id = ?", (balance_change, self.card_id))

            # --- Insert Transaction Record in DB ---
            cursor.execute("""
                INSERT INTO transactions (card_id, transaction_type, amount)
                VALUES (?, ?, ?)
            """, (self.card_id, transaction_type, amount))

            conn.commit()
            success = True
            print(f"Transaction successful: {transaction_type} ${amount}")

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"Transaction failed: {e}")
            print(f"Database error during transaction: {e}")
            if conn: conn.rollback() # Rollback changes on error
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An unexpected error occurred: {e}")
            print(f"An error occurred during transaction: {e}")
            if conn: conn.rollback()
        finally:
            if conn:
                conn.close()

        if success:
             # --- Refresh UI ---
             self.load_card_details() # Reload details to get updated balance and lock status
             self.load_transactions() # Reload transaction list
        return success


    def handle_deposit(self):
        """Handles the deposit button click."""
        if self.is_locked:
             QMessageBox.warning(self, "Card Locked", "Cannot deposit while card is locked.")
             return

        amount, ok = QInputDialog.getDouble(self, "Deposit", "Enter amount to deposit:", decimals=2, min=0.01)
        if ok and amount > 0:
            self.perform_transaction('deposit', amount)
            # UI refresh is handled within perform_transaction on success

    def handle_withdraw(self):
        """Handles the withdraw button click."""
        if self.is_locked:
             QMessageBox.warning(self, "Card Locked", "Cannot withdraw while card is locked.")
             return

        amount, ok = QInputDialog.getDouble(self, "Withdraw", "Enter amount to withdraw:", decimals=2, min=0.01)
        if ok and amount > 0:
            # Check sufficient funds *before* calling perform_transaction
            if amount > self.balance:
                QMessageBox.warning(self, "Error", "Insufficient funds.")
            else:
                self.perform_transaction('withdrawal', amount)
                # UI refresh is handled within perform_transaction on success

    def handle_transfer(self):
        """Handles the transfer button click."""
        if self.is_locked:
             QMessageBox.warning(self, "Card Locked", "Cannot transfer while card is locked.")
             return

        # NOTE: This is a simplified transfer (just deducts).
        # A real app would need destination account details.
        amount, ok = QInputDialog.getDouble(self, "Transfer", "Enter amount to transfer:", decimals=2, min=0.01)
        if ok and amount > 0:
             # Check sufficient funds *before* calling perform_transaction
            if amount > self.balance:
                QMessageBox.warning(self, "Error", "Insufficient funds for transfer.")
            else:
                # We log it as 'transfer' but it just deducts balance here
                self.perform_transaction('transfer', amount)
                # UI refresh is handled within perform_transaction on success

    def open_manage_card(self):
        """Opens the manage card dialog."""
        # Pass card_id and self (main window instance) to the manage window
        self.manage_window = ManageCardWindow(self.card_id, self)
        self.manage_window.show()


def main():
    # This main function is primarily for testing this window in isolation
    app = QApplication(sys.argv)
    # Provide a dummy card_id for testing - make sure this ID exists in your cards table
    test_card_id = 1
    window = MainWindow(test_card_id)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()