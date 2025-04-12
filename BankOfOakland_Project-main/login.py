import sys, os
from PyQt5.QtWidgets import *
##Libraries used##: QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QLineEdit, QSizePolicy
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

# --- Imports Added ---
import sqlite3
import hashlib # Although not used for login check now due to vulnerability, keep for later
# --- End Imports Added ---

# --- Make sure these imports point to the correct files ---
import db # Assuming db.py is in the same directory
import accountCreation # Assuming accountCreation.py is in the same directory
import cardSelection # Assuming cardSelection.py is in the same directory
# --- End Imports Check ---


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bank of Oakland: Login")
        self.setFixedSize(400, 550) #(x, y, width, height)
        # Ensure placeholder.jpg is in the same directory or provide a full path
        icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "placeholder.jpg")
        if os.path.exists(icon_path):
             self.setWindowIcon(QIcon(icon_path))
        else:
             print(f"Warning: Icon file not found at {icon_path}")

        #Declares all GUI elements

        #Login GUI
        #Text
        #Static text
        self.welcomeLbl = QLabel("Bank of Oakland", self)
        self.usrLbl = QLabel("Username: ", self)
        self.passLbl = QLabel("Password: ", self)

        #State text
        self.changeable = QLabel("", self) # Changed placeholder

        #Images
        self.appLogo = QLabel(self)

        #Buttons
        self.loginBtn = QPushButton("Login!", self)
        self.createBtn = QPushButton("Create account!", self)

        #EntryFields
        self.userEntry = QLineEdit(self)
        self.passEntry = QLineEdit(self)
        self.passEntry.setEchoMode(QLineEdit.Password) # Hide password input

        #New Account GUI
        ##!!!This is subject for removal!!!##

        #Starts the GUI
        self.initLoginUI()

    #Login UI Initialize
    def initLoginUI(self):
        #Attribute setters
        # Ensure placeholder.jpg is in the same directory or provide a full path
        icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "placeholder.jpg")
        if os.path.exists(icon_path):
            iconIMG = QPixmap(icon_path)
            self.appLogo.setPixmap(iconIMG)
        else:
            self.appLogo.setText("Icon Missing") # Placeholder text if image fails
            print(f"Warning: Icon file not found at {icon_path}")

        self.appLogo.setScaledContents(True)
        self.appLogo.setGeometry(100, 40, 201, 181)
        self.appLogo.setAlignment(Qt.AlignCenter)
        self.userEntry.setGeometry(100, 330, 201, 31)
        font = QFont()
        font.setPointSize(10)
        self.userEntry.setFont(font)
        self.passEntry.setGeometry(100, 410, 201, 31)
        self.passEntry.setFont(font)
        self.loginBtn.setGeometry(140, 460, 121, 31)
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.loginBtn.setFont(font1)
        self.welcomeLbl.setEnabled(True)
        self.welcomeLbl.setGeometry(20, 250, 351, 31)
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setWeight(75)
        self.welcomeLbl.setFont(font2)
        self.welcomeLbl.setScaledContents(False)
        self.welcomeLbl.setAlignment(Qt.AlignCenter)
        self.changeable.setGeometry(140, 500, 121, 20)
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(True)
        font3.setWeight(50)
        self.changeable.setFont(font3)
        self.changeable.setAlignment(Qt.AlignCenter)
        self.createBtn.setGeometry(290, 512, 91, 21)
        self.usrLbl.setGeometry(100, 310, 201, 16)
        font4 = QFont()
        font4.setPointSize(12)
        self.usrLbl.setFont(font4)
        self.passLbl.setGeometry(100, 390, 201, 16)
        self.passLbl.setFont(font4)

        #Button mapping
        self.loginBtn.clicked.connect(self.loginPress)
        self.createBtn.clicked.connect(self.newPress)

    #Button functions
    def loginPress(self):
        username = self.userEntry.text()
        password = self.passEntry.text()
        self.changeable.setText("") # Clear previous messages

        if not username or not password:
            self.changeable.setText("Enter username/password")
            return

        conn = None # Initialize conn to None
        try:
            # --- Database Connection ---
            db_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bank.db")
            if not os.path.exists(db_file):
                 self.changeable.setText("Database file not found!")
                 return
            conn = sqlite3.connect(db_file)
            cursor = conn.cursor()

            # --- Fetch User ---
            # Using parameterization even here is good practice, though the vulnerability is in accountCreation
            cursor.execute("SELECT id, password_hash FROM users WHERE username = ?", (username,))
            user_record = cursor.fetchone()

            if user_record:
                user_id = user_record[0]
                stored_password = user_record[1] # This is the plain text password due to the vulnerability

                # --- Password Verification (Plain Text Comparison) ---
                # IMPORTANT: This compares plain text passwords because accountCreation stores them plainly.
                # For a secure app, you would hash the entered password and compare hashes.
                if password == stored_password:
                    print(f"Logging in as user ID: {user_id}")
                    self.changeable.setText("Login Successful!")

                    # --- Open cardSelection window ---
                    # Pass the user_id to the cardSelection window
                    self.cardSelectionWindow = cardSelection.cardSelection(user_id)
                    self.cardSelectionWindow.show()
                    self.close() # Close login window

                else:
                    self.changeable.setText("Invalid username or password")
            else:
                self.changeable.setText("Invalid username or password")

        except sqlite3.Error as e:
            print("Database error during login:", e)
            self.changeable.setText("Database error occurred")
        except Exception as e:
             print("An error occurred:", e)
             self.changeable.setText("An error occurred")
        finally:
            if conn:
                conn.close() # Ensure connection is closed

    def newPress(self):
        # Pass self (the login window instance) to allow accountCreation to call accountFlag
        self.accountCreationWindow = accountCreation.accountWindow(self)
        self.accountCreationWindow.show()

    def accountFlag(self, username):
        self.changeable.setText("Welcome " + username + "!")
        # Clear password field after successful creation for better UX
        self.passEntry.clear()
        self.userEntry.setText(username) # Pre-fill username

def main():
    # --- Initialize DB if it doesn't exist ---
    db_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bank.db")
    if not os.path.exists(db_file):
         print("Database not found, initializing...")
         db.initializeDB()
    else:
         print("Database found.")
    # --- End DB Init ---

    app = QApplication(sys.argv)
    loginWindow = MainWindow()
    loginWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()