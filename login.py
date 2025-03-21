import sys, os
from PyQt5.QtWidgets import *
##Libraries used##: QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QLineEdit, QSizePolicy
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

import accountCreation 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bank of Oakland: Login")
        self.setFixedSize(400, 550) #(x, y, width, height)
        self.setWindowIcon(QIcon("placeholder.jpg")) #File must be in the same directory
#Declares all GUI elements

#Login GUI
    #Text
        #Static text
        self.welcomeLbl = QLabel("Bank of Oakland", self)
        self.usrLbl = QLabel("Username: ", self)
        self.passLbl = QLabel("Password: ", self)

        #State text
        self.changeable = QLabel("placeholder", self)

    #Images
        self.appLogo = QLabel(self)

    #Buttons
        self.loginBtn = QPushButton("Login!", self)
        self.createBtn = QPushButton("Create account!", self)

    #EntryFields
        self.userEntry = QLineEdit(self)
        self.passEntry = QLineEdit(self)

#New Account GUI
    ##!!!This is subject for removal!!!##

#Starts the GUI
        self.initLoginUI()

#Login UI Initialize
    def initLoginUI(self):
    #Positions all the nodes
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

    #Attribute setters
        #Image retriever
        iconIMG = QPixmap("placeholder.jpg")
        self.appLogo.setPixmap(iconIMG)
        self.appLogo.setScaledContents(True)

        #Button mapping
        self.loginBtn.clicked.connect(self.loginPress)
        self.createBtn.clicked.connect(self.newPress)



#New Account UI Initialize

#Button functions
    def loginPress(self):
          username = self.userEntry.text()    
          password = self.passEntry.text()
          
          #Testing stuff
          self.changeable.setText("Pressed")
          print(str(username) + " " + str(password))
    
    def newPress(self):
          accountCreation.main()

def main():
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())

if __name__ == "__main__":
        main()
        