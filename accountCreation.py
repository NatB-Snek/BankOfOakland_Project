import sys, os
from PyQt5.QtWidgets import *
##Libraries used##: QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QLineEdit, QSizePolicy
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt


class MainWindow(QWidget):
        def __init__(self):
                super().__init__()
                self.setWindowTitle("Bank of Oakland: Account Creation")
                self.setFixedSize(400, 550) #(x, y, width, height)
                self.setWindowIcon(QIcon("placeholder.jpg")) #File must be in the same directory
        #Declorations
                self.userEntry = QTextEdit(self)
                self.passEntry = QTextEdit(self)
                self.firstEntry = QTextEdit(self)
                self.lastEntry = QTextEdit(self)
                self.birthdayDate = QDateEdit(self)
                self.emailEntry = QTextEdit(self)
                self.passConfEntry = QTextEdit(self)

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
                self.changeableLbl = QLabel("For demo purposes, \nbirthday and email arent used", self)

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
                self.userEntry.setMidLineWidth(0)
                self.passEntry.setGeometry(160, 120, 201, 31)
                font1 = QFont()
                font1.setPointSize(10)
                self.passEntry.setFont(font1)
                self.createBtn.setGeometry(20, 440, 121, 31)
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
                self.passConfEntry.setGeometry(160, 170, 201, 31)
                self.passConfEntry.setFont(font1)
                self.passConfLbl.setGeometry(20, 170, 111, 31)
                self.passConfLbl.setFont(font1)
                self.passConfLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        #Placements and attributes
                

        #

        def createClick():
                
                pass

        def backClick():

                pass

                

def main():
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())

if __name__ == "__main__":
        main()
        