

### !!!NOTE!!! ###
#This is if we have time to add these functions, this was mainly added for the "delete" function 


import sys, os
from PyQt5.QtWidgets import *
##Libraries used##: QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QLineEdit, QSizePolicy
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bank of Oakland: Manage Card")
        self.setFixedSize(250, 250) #(x, y, width, height)
        self.setWindowIcon(QIcon("placeholder.jpg")) #File must be in the same directory

        #Declare
        self.lockBtn = QPushButton("Lock Card", self)
        self.lockBtn.setGeometry(20, 100, 141, 23)

        self.unlockCkBx = QCheckBox("Unlock Options", self)
        self.unlockCkBx.setGeometry(130, 180, 111, 61)

        self.deleteBtn = QPushButton("Delete Card", self)
        self.deleteBtn.setGeometry(20, 140, 141, 23)

        self.okBtn = QPushButton("Ok", self)
        self.okBtn.setGeometry(40, 200, 75, 23)

        self.renameBtn = QPushButton("Rename", self)
        self.renameBtn.setGeometry(20, 20, 75, 23)

        self.renameInputReciever = QLineEdit(self)
        self.renameInputReciever.setGeometry(120, 20, 113, 20)
        
        self.cleanBtn = QPushButton("Clean History", self)
        self.cleanBtn.setGeometry(20, 60, 141, 23)


def main():
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())

if __name__ == "__main__":
        main()