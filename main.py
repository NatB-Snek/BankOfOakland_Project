### !!!NOTE!!! ###
#None of this actually works yet, needs to be formated (at least after line 26)

import sys, os
from PyQt5.QtWidgets import *
##Libraries used##: QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QLineEdit, QSizePolicy
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt, QRect

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bank of Oakland: <Account Number>")
        self.setFixedSize(830, 520) #(x, y, width, height)
        self.setWindowIcon(QIcon("placeholder.jpg")) #File must be in the same directory
    
        #DeclareValues

        self.balanceStaticLbl = QLabel("Balance:",self)
        self.balanceLbl = QLabel("X,XXX,XXX", self) #This wont be static
        self.accountStaticLbl = QLabel("Account Number:",self)
        self.accountInfoLbl = QLabel("<Card name> <Account Holder Name>", self)
        self.transactionsList = QListWidget(self)
        self.transactionsStaticLbl = QLabel("Transactions:",self)
        self.depositBtn = QPushButton("Deposit", self)
        self.accountLbl = QLabel("XXXXXXXXX", self)
        self.routingLbl = QLabel("XXXXXXXXX", self)
        self.routingStaticLbl = QLabel("Routing Number:", self)
        self.transferBtn = QPushButton("Transfer", self)
        self.manageCardBtn = QPushButton("Manage Card", self)
        self.withdrawBtn = QPushButton("Withdraw", self)

        self.initUi()

    
    def initUi(self):
        self.balanceStaticLbl.setGeometry(QRect(40, 30, 181, 40))
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.balanceStaticLbl.setFont(font)
        self.balanceLbl.setGeometry(QRect(230, 30, 310, 40))
        self.balanceLbl.setFont(font)
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
        self.accountLbl.setGeometry(QRect(260, 430, 151, 41))
        self.accountLbl.setFont(font1)
        self.routingStaticLbl.setGeometry(QRect(40, 470, 211, 41))
        self.routingStaticLbl.setFont(font1)
        self.routingLbl.setGeometry(QRect(260, 470, 151, 41))
        self.routingLbl.setFont(font1)
        self.withdrawBtn.setGeometry(QRect(40, 190, 331, 51))
        self.withdrawBtn.setFont(font3)
        self.transferBtn.setGeometry(QRect(40, 260, 331, 51))
        self.transferBtn.setFont(font3)
        self.manageCardBtn.setGeometry(QRect(40, 330, 331, 51))
        self.manageCardBtn.setFont(font3)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
