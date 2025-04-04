import sys, os
from PyQt5.QtWidgets import *
##Libraries used##: QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QLineEdit, QSizePolicy
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

import sqlite3
import hashlib

import login


class accountWindow(QWidget):
        def __init__(self, loginWindow):
                super().__init__()
                self.loginWindow = loginWindow
                self.setWindowTitle("Bank of Oakland: Account Creation")
                self.setFixedSize(400, 550) #(x, y, width, height)
                self.setWindowIcon(QIcon("placeholder.jpg")) #File must be in the same directory
        #Declorations
                self.userEntry = QLineEdit(self)
                self.passEntry = QLineEdit(self)
                self.firstEntry = QLineEdit(self)
                self.lastEntry = QLineEdit(self)
                self.birthdayDate = QDateEdit(self)
                self.emailEntry = QLineEdit(self)
                self.passConfEntry = QLineEdit(self)

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
                self.changeableLbl = QLabel("", self)

        #Variables
                self.user = ""
                self.password = ""
                self.confirmPassword = ""

                #These really arnt that neccecary but just in case
                self.first = ""
                self.last = ""
                self.birthday = ""
                self.email = ""

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
                self.checkBox.setGeometry(160, 440, 111, 31)
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
                self.cancelBtn.clicked.connect(self.backClick)
                self.createBtn.clicked.connect(self.createClick)

        def createClick(self):
                user = self.userEntry.text()
                password = self.passEntry.text()
                confirmPassword = self.passConfEntry.text()
                first = self.firstEntry.text()
                last = self.lastEntry.text()
                birthday = self.birthdayDate.date().toString("MM-dd-yyyy")
                email = self.emailEntry.text()

                check1 = True
                check2 = password == confirmPassword

                if not check2:
                        self.changeableLbl.setText("Passwords Don't Match!")
                        return

                if check1 and check2:
                        try:
                                conn = sqlite3.connect("bank.db")
                                cursor = conn.cursor()

                        # Insecure raw SQL formatting (intentional for SQL injection demo)
                                raw_query = f"INSERT INTO users (username, password_hash, email, firstname, lastname, birthday) VALUES ('{user}', '{password}', '{email}', '{first}', '{last}', '{birthday}')"
                                print("[DEBUG] Executing:", raw_query)
                                cursor.execute(raw_query)
                                conn.commit()

                                self.loginWindow.accountFlag(user)
                                self.close()
                        except sqlite3.Error as err:
                                print("Error during user creation:", err)
                                self.changeableLbl.setText("Database Error")
                        finally:
                                if conn:
                                        cursor.close()
                                        conn.close()

        def backClick(self):
                self.close()

def main():

        app = QApplication(sys.argv)
        window = accountWindow()
        window.show()
        sys.exit(app.exec_())

        return window

if __name__ == "__main__":
        main()
        