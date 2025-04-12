import sys, os
from PyQt5.QtWidgets import *
##Libraries used##: QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QLineEdit, QSizePolicy, QWidget, QScrollArea, QGroupBox, QFormLayout, QDialog # Added necessary layout/widget imports
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

# --- Imports Added ---
import sqlite3
import random
import datetime
# --- End Imports Added ---

# --- Make sure main.py is importable ---
from main import MainWindow # Assuming main.py contains MainWindow
# --- End Import Check ---

class cardSelection(QMainWindow):
    def __init__(self, user_id): # Accept user_id from login
        super().__init__()
        self.user_id = user_id # Store user_id
        self.setWindowTitle("Bank of Oakland: Card Selection")
        self.setFixedSize(400, 550)
        # Ensure placeholder.jpg is in the same directory or provide a full path
        icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "placeholder.jpg")
        if os.path.exists(icon_path):
             self.setWindowIcon(QIcon(icon_path))
        else:
             print(f"Warning: Icon file not found at {icon_path}")
        self.font = QFont()

        self.username = self.fetch_username() # Fetch username based on user_id

        self.addBtn = QPushButton("New Card", self)
        self.titleLbl = QLabel("Bank of Oakland \nB O O", self)
        self.lbl2 = QLabel(f"Cards for: {self.username}", self) # Display fetched username

        # --- Layout Setup ---
        self.centralWidget = QWidget(self) # Create a central widget
        self.setCentralWidget(self.centralWidget) # Set it for the main window
        self.mainLayout = QVBoxLayout(self.centralWidget) # Main layout for the central widget

        self.formLayout = QFormLayout() # Layout for card rows
        self.groupBox = QGroupBox("Your Accounts:") # Group box to hold card rows
        self.groupBox.setLayout(self.formLayout) # Set layout for group box

        self.scroll = QScrollArea(self) # Scroll area for the group box
        self.scroll.setWidget(self.groupBox) # Put group box inside scroll area
        self.scroll.setWidgetResizable(True) # Allow group box to resize
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff) # Hide horizontal scroll bar
        # --- End Layout Setup ---

        self.initUI()
        self.load_cards() # Load cards after UI is initialized

    def fetch_username(self):
        """Fetches the username from the database based on user_id."""
        username = "Unknown User"
        conn = None
        try:
            db_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bank.db")
            if not os.path.exists(db_file): return username # Return default if DB not found
            conn = sqlite3.connect(db_file)
            cursor = conn.cursor()
            cursor.execute("SELECT username FROM users WHERE id = ?", (self.user_id,))
            result = cursor.fetchone()
            if result:
                username = result[0]
        except sqlite3.Error as e:
            print(f"Database error fetching username: {e}")
        except Exception as e:
            print(f"An error occurred fetching username: {e}")
        finally:
            if conn:
                conn.close()
        return username

    def initUI(self):
        # --- Arrange Widgets using Layouts ---
        # Title and User Label
        self.titleLbl.setAlignment(Qt.AlignCenter)
        self.titleLbl.setStyleSheet("font-weight: bold;")
        font_title = QFont()
        font_title.setPointSize(16)
        self.titleLbl.setFont(font_title)

        self.lbl2.setAlignment(Qt.AlignCenter)
        font_user = QFont()
        font_user.setPointSize(11)
        self.lbl2.setFont(font_user)

        # Add Title, User Label, Scroll Area, and Button to the main layout
        self.mainLayout.addWidget(self.titleLbl)
        self.mainLayout.addWidget(self.lbl2)
        self.mainLayout.addWidget(self.scroll) # Add scroll area
        self.mainLayout.addWidget(self.addBtn, alignment=Qt.AlignCenter) # Add button, centered

        # Adjust spacing/margins if needed
        self.mainLayout.setContentsMargins(20, 20, 20, 20) # Add some padding
        self.mainLayout.setSpacing(15) # Spacing between widgets

        # --- End Layout Arrangement ---

        # --- Removed absolute positioning (setGeometry) ---

        # Button Connection
        self.addBtn.clicked.connect(self.addClicked)

        # Set vertical spacing within the form layout inside the group box
        self.formLayout.setVerticalSpacing(15)


    def load_cards(self):
        """Fetches cards from DB and adds them to the UI."""
        # Clear existing rows first (important if re-loading)
        while self.formLayout.count():
             item = self.formLayout.takeAt(0)
             widget = item.widget()
             if widget:
                 widget.deleteLater()

        conn = None
        try:
             db_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bank.db")
             if not os.path.exists(db_file):
                 print("Database not found for loading cards.")
                 # Optionally add a label indicating no DB connection
                 return
             conn = sqlite3.connect(db_file)
             cursor = conn.cursor()

             cursor.execute("SELECT id, card_number, balance FROM cards WHERE user_id = ?", (self.user_id,))
             cards = cursor.fetchall()

             if not cards:
                 # Add a label if no cards are found
                 no_cards_label = QLabel("No cards found. Click 'New Card' to add one.")
                 no_cards_label.setAlignment(Qt.AlignCenter)
                 self.formLayout.addRow(no_cards_label)
             else:
                 for card in cards:
                      card_id, card_number, balance = card
                      self.addCardRow(card_id, card_number, balance)

             # Adjust group box size after adding rows
             self.groupBox.adjustSize()

        except sqlite3.Error as e:
             print(f"Database error loading cards: {e}")
             # Optionally add a label indicating DB error
        except Exception as e:
             print(f"An error occurred loading cards: {e}")
        finally:
             if conn:
                  conn.close()

    def addCardRow(self, card_id, card_number, balance):
        """Adds a row representing a card to the form layout."""
        # Use last 4 digits of card number
        last_four_digits = card_number[-4:] if len(card_number) >= 4 else card_number

        balanceLabel = QLabel("Balance:")
        balanceAmount = QLabel(f"${balance:,.2f}") # Format balance
        cardButton = QPushButton(f"**** {last_four_digits}")
        cardButton.setToolTip(f"View details for card ending in {last_four_digits}") # Tooltip

        # Sizing and Font
        cardButton.setFixedHeight(40)
        # cardButton.setFixedWidth(120) # Let layout handle width generally
        font = QFont()
        font.setPointSize(10)
        balanceLabel.setFont(font)
        balanceAmount.setFont(font)
        cardButton.setFont(font)

        # Connect button click, passing card_id
        cardButton.clicked.connect(lambda _, cid=card_id: self.openMainWindow(cid))

        # Layout for the row
        rowLayout = QHBoxLayout()
        rowLayout.addWidget(balanceLabel)
        rowLayout.addWidget(balanceAmount)
        rowLayout.addStretch() # Pushes button to the right
        rowLayout.addWidget(cardButton)

        # Add the row layout to the form layout
        self.formLayout.addRow(rowLayout)


    def addClicked(self):
        """Handles the 'New Card' button click."""
        self.openAddCardDialog()

    def openMainWindow(self, card_id):
        """Opens the main account window for the selected card."""
        print(f"Opening main window for card ID: {card_id}")
        # Pass card_id to the main window
        self.mainWindow = MainWindow(card_id)
        self.mainWindow.show()
        # Consider closing this window or hiding it
        # self.close() or self.hide()

    def openAddCardDialog(self):
        """Opens a dialog to confirm adding a new card."""
        dialog = QDialog(self)
        dialog.setWindowTitle("Add New Card")
        dialog.setFixedSize(250, 150)

        layout = QVBoxLayout()
        label = QLabel("Are you sure you want to add a new card?")
        layout.addWidget(label)

        buttonLayout = QHBoxLayout()
        confirmButton = QPushButton("Confirm")
        cancelButton = QPushButton("Cancel")
        buttonLayout.addWidget(confirmButton)
        buttonLayout.addWidget(cancelButton)

        layout.addLayout(buttonLayout)
        dialog.setLayout(layout)

        # Connect buttons to dialog actions
        confirmButton.clicked.connect(lambda: self.confirmAddCard(dialog))
        cancelButton.clicked.connect(dialog.reject) # Close dialog without action

        dialog.exec_() # Show the dialog modally

    def confirmAddCard(self, dialog):
        """Creates a new card record in the database and updates the UI."""
        conn = None
        try:
            # Generate new card details
            # Routing Numbers
            new_card_number = str(random.randint(1000000000000000, 9999999999999999))
            new_cvv = str(random.randint(100, 999))
            new_expiry_date = (datetime.date.today() + datetime.timedelta(days=3*365)).strftime('%Y-%m-%d') # 3 years expiry
            new_account_num = random.randint(100000000, 999999999)
            new_routing_num = random.randint(100000000, 999999999)
            initial_balance = 0.00

            # --- Database Interaction ---
            db_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bank.db")
            if not os.path.exists(db_file):
                 QMessageBox.warning(self, "Error", "Database file not found.")
                 dialog.reject()
                 return

            conn = sqlite3.connect(db_file)
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO cards
                (user_id, card_number, accountNum, routingNum, cvv, expiry_date, balance, isLocked)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (self.user_id, new_card_number, new_account_num, new_routing_num, new_cvv, new_expiry_date, initial_balance, 0)) # Start unlocked

            conn.commit()
            new_card_id = cursor.lastrowid # Get the ID of the new card
            print(f"New card created with ID: {new_card_id}")

            # --- Update UI ---
            if self.formLayout.rowCount() > 0:
                 item = self.formLayout.itemAt(0)
                 if isinstance(item.widget(), QLabel) and "No cards found" in item.widget().text():
                      widget = self.formLayout.takeAt(0).widget()
                      if widget: widget.deleteLater()

            self.addCardRow(new_card_id, new_card_number, initial_balance)
            self.groupBox.adjustSize() # Adjust size after adding

            dialog.accept() # Close the confirmation dialog

        except sqlite3.IntegrityError:
             QMessageBox.warning(self, "Error", "Failed to create card. Card number might already exist.")
             print("Database integrity error creating card (likely duplicate card number)")
             dialog.reject()
        except sqlite3.Error as e:
             QMessageBox.warning(self, "Error", f"Database error creating card: {e}")
             print(f"Database error creating card: {e}")
             dialog.reject()
        except Exception as e:
             QMessageBox.critical(self, "Error", f"An unexpected error occurred: {e}")
             print(f"An unexpected error occurred creating card: {e}")
             dialog.reject()
        finally:
            if conn:
                conn.close()


def main():
    # This main function is primarily for testing this window in isolation
    app = QApplication(sys.argv)
    # Provide a dummy user_id for testing
    test_user_id = 1 # Assume a user with ID 1 exists in your test DB
    window = cardSelection(test_user_id)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()