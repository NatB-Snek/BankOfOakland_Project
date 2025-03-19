import sys, os
from PyQt5.QtWidgets import *
##Libraries used##: QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QLineEdit, QSizePolicy
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

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
        self.createBtn = QPushButton("Create new account!", self)

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
        self.appLogo.setGeometry(100, 50, 200, 180)
        self.appLogo.setAlignment(Qt.AlignCenter)
        self.welcomeLbl.setGeometry(100, 250, 201, 20)
        self.welcomeLbl.setAlignment(Qt.AlignCenter)
        self.changeable.setGeometry(140, 490, 121, 20)
        self.changeable.setAlignment(Qt.AlignCenter)
        self.userEntry.setGeometry(100, 300, 201, 41)
        self.passEntry.setGeometry(100, 380, 201, 41)
        self.loginBtn.setGeometry(140, 450, 121, 31)
        self.createBtn.setGeometry(270, 510, 111, 23)
        self.usrLbl.setGeometry(100, 280, 47, 13)
        self.passLbl.setGeometry(100, 360, 47, 13)

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
          print("funtionality soon")

def main():
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())

if __name__ == "__main__":
        main()
        