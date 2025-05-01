import sys, os
from PyQt5.QtWidgets import *
##Libraries used##: QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QLineEdit, QSizePolicy, QDateEdit
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt, QDate # Added QDate

# --- Imports Added ---
import sqlite3
import hashlib # Not used for saving, but good practice to import if hashing is intended later
# --- End Imports Added ---

# --- Assuming login.py is in the same directory or accessible ---
# import login # No need to import login, it's passed in __init__
# ---

class accountWindow(QWidget):
    def __init__(self, loginWindow): # Accepts the login window instance
        super().__init__()
        self.loginWindow = loginWindow # Store the reference
        self.setWindowTitle("Bank of Oakland: Account Creation")
        self.setFixedSize(400, 550) #(x, y, width, height)
        # Ensure placeholder.jpg is in the same directory or provide a full path
        icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "placeholder.jpg")
        if os.path.exists(icon_path):
             self.setWindowIcon(QIcon(icon_path))
        else:
             print(f"Warning: Icon file not found at {icon_path}")

        #Declorations
        self.userEntry = QLineEdit(self)
        self.passEntry = QLineEdit(self)
        self.passEntry.setEchoMode(QLineEdit.Password) # Hide password
        self.firstEntry = QLineEdit(self)
        self.lastEntry = QLineEdit(self)
        self.birthdayDate = QDateEdit(self)
        self.birthdayDate.setDisplayFormat("MM-dd-yyyy") # Set display format
        self.birthdayDate.setCalendarPopup(True) # Enable calendar popup
        self.birthdayDate.setDate(QDate.currentDate().addYears(-18)) # Default to 18 years ago
        self.emailEntry = QLineEdit(self)
        self.passConfEntry = QLineEdit(self)
        self.passConfEntry.setEchoMode(QLineEdit.Password) # Hide password confirmation

        self.checkBox = QCheckBox("Agree to Terms of Service", self)
        self.createBtn = QPushButton("Create!", self)
        self.cancelBtn = QPushButton("Cancel", self)

        self.titleLbl = QLabel("Account Creation", self)
        self.userLbl = QLabel("Username:", self)
        self.passLbl = QLabel("Password:", self)
        self.passConfLbl = QLabel("Confirm Password:", self)
        self.firstLbl = QLabel("First Name:", self)
        self.lastLbl = QLabel("Last Name:", self)
        self.birthLbl = QLabel("Birthday:", self)
        self.emailLbl = QLabel("Email:", self)
        self.changeableLbl = QLabel("", self) # Status label

        #Variables are directly read from widgets in createClick

        self.initUI()

    def initUI(self):
        #Set Attriutes
        self.userEntry.setGeometry(160, 70, 201, 31)
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.userEntry.setFont(font)
        #self.userEntry.setMidLineWidth(0)
        self.passEntry.setGeometry(160, 120, 201, 31)
        font1 = QFont()
        font1.setPointSize(10)
        self.passEntry.setFont(font1)
        self.createBtn.setGeometry(20, 440, 121, 31)
        self.passConfEntry.setGeometry(160, 170, 201, 31)
        self.passConfEntry.setFont(font1)
        self.passConfLbl.setGeometry(20, 170, 111, 31)
        self.passConfLbl.setFont(font1)
        self.passConfLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        font2 = QFont()
        font2.setPointSize(12)
        self.createBtn.setFont(font2)
        self.userLbl.setGeometry(20, 70, 111, 31)
        self.userLbl.setFont(font1)
        self.userLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.firstEntry.setGeometry(160, 220, 201, 31)
        self.firstEntry.setFont(font1)
        self.lastEntry.setGeometry(160, 270, 201, 31)
        self.lastEntry.setFont(font1)
        self.emailEntry.setGeometry(160, 370, 201, 31)
        self.emailEntry.setFont(font1)
        self.checkBox.setGeometry(160, 440, 161, 31) # Increased width for text
        self.checkBox.setFont(font1)
        self.cancelBtn.setGeometry(20, 490, 121, 31)
        self.cancelBtn.setFont(font2)
        self.passLbl.setGeometry(20, 120, 111, 31)
        self.passLbl.setFont(font1)
        self.passLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.firstLbl.setGeometry(20, 220, 111, 31)
        self.firstLbl.setFont(font1)
        self.firstLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.birthLbl.setGeometry(20, 320, 111, 31)
        self.birthLbl.setFont(font1)
        self.birthLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.emailLbl.setGeometry(20, 370, 111, 31)
        self.emailLbl.setFont(font1)
        self.emailLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.changeableLbl.setGeometry(160, 490, 200, 30)
        self.changeableLbl.setFont(font1)
        self.changeableLbl.setAlignment(Qt.AlignCenter) # Center align status text
        self.titleLbl.setGeometry(130, 30, 141, 20)
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.titleLbl.setFont(font3)
        self.titleLbl.setAlignment(Qt.AlignCenter)
        self.lastLbl.setGeometry(20, 270, 111, 31)
        self.lastLbl.setFont(font1)
        self.lastLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.birthdayDate.setGeometry(160, 320, 201, 31)
        self.birthdayDate.setFont(font1)

        # Connect buttons
        self.cancelBtn.clicked.connect(self.backClick)
        self.createBtn.clicked.connect(self.createClick)

    def createClick(self):
        self.changeableLbl.setText("") # Clear previous messages
        user = self.userEntry.text().strip()
        password = self.passEntry.text() # Get password (not stripped intentionally for demo)
        confirmPassword = self.passConfEntry.text()
        first = self.firstEntry.text().strip()
        last = self.lastEntry.text().strip()
        birthday = self.birthdayDate.date().toString("yyyy-MM-dd") # Use standard ISO format
        email = self.emailEntry.text().strip()

        # --- Input Validation ---
        if not all([user, password, confirmPassword, first, last, email]):
             self.changeableLbl.setText("All fields are required!")
             return
        if password != confirmPassword:
            self.changeableLbl.setText("Passwords Don't Match!")
            return
        if not self.checkBox.isChecked():
             self.changeableLbl.setText("Agree to ToS!")
             return
        # --- End Input Validation ---

        conn = None # Initialize conn
        try:
            # --- Database Connection ---
            db_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bank.db")
            if not os.path.exists(db_file):
                 self.changeableLbl.setText("Database file not found!")
                 return
            conn = sqlite3.connect(db_file)
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO users (username, password_hash, email, firstname, lastname, birthday)
                VALUES (?, ?, ?, ?, ?, ?)""",
                (user, password, email, first, last, birthday))

            conn.commit() # Commit the changes

            # --- Success ---
            print("User created successfully:", user)
            if self.loginWindow:
                 self.loginWindow.accountFlag(user) # Update login window status
            self.close() # Close the account creation window

        except sqlite3.IntegrityError:
             # Handle cases where username or email might already exist (UNIQUE constraint)
             self.changeableLbl.setText("Username or Email already exists!")
             print("Database integrity error (likely duplicate username/email)")
        except sqlite3.Error as err:
            print("Error during user creation:", err)
            self.changeableLbl.setText("Database Error")
        except Exception as e:
            print("An unexpected error occurred:", e)
            self.changeableLbl.setText("An error occurred")
        finally:
            if conn:
                conn.close() # Ensure connection is always closed

    def backClick(self):
        self.close() # Close the window

def main():
        # This main function is primarily for testing this window in isolation
        # Normally, it's opened from the login window
        app = QApplication(sys.argv)
        # Create a dummy login window instance if running standalone
        # This avoids errors but the accountFlag call won't do anything useful
        class DummyLogin:
             def accountFlag(self, username):
                  print(f"Account created for {username} (Dummy Login Window)")
        dummy_login = DummyLogin()
        window = accountWindow(dummy_login)
        window.show()
        sys.exit(app.exec_())

if __name__ == "__main__":
        main()