### !!!NOTE!!! ###
#None of this actually works yet, needs to be formated (at least after line 26)

import sys, os
from PyQt5.QtWidgets import *
##Libraries used##: QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QLineEdit, QSizePolicy
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bank of Oakland: Account Creation")
        self.setFixedSize(400, 550) #(x, y, width, height)
        self.setWindowIcon(QIcon("placeholder.jpg")) #File must be in the same directory



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

#This needs to be sorted
"""
class Ui_self(object):
    def setupUi(self, self):
        if self.objectName():
            self.setObjectName(u"self")
        self.resize(829, 518)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.balanceStaticLbl = QLabel(self.centralwidget)
        self.balanceStaticLbl.setObjectName(u"balanceStaticLbl")
        self.balanceStaticLbl.setGeometry(QRect(40, 30, 181, 40))
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.balanceStaticLbl.setFont(font)
        self.balanceLbl = QLabel(self.centralwidget)
        self.balanceLbl.setObjectName(u"balanceLbl")
        self.balanceLbl.setGeometry(QRect(230, 30, 310, 40))
        self.balanceLbl.setFont(font)
        self.accountStaticLbl = QLabel(self.centralwidget)
        self.accountStaticLbl.setObjectName(u"accountStaticLbl")
        self.accountStaticLbl.setGeometry(QRect(40, 430, 211, 41))
        font1 = QFont()
        font1.setPointSize(20)
        self.accountStaticLbl.setFont(font1)
        self.accountInfoLbl = QLabel(self.centralwidget)
        self.accountInfoLbl.setObjectName(u"accountInfoLbl")
        self.accountInfoLbl.setGeometry(QRect(40, 80, 461, 31))
        font2 = QFont()
        font2.setPointSize(15)
        font2.setItalic(False)
        self.accountInfoLbl.setFont(font2)
        self.transactionsList = QListWidget(self.centralwidget)
        self.transactionsList.setObjectName(u"transactionsList")
        self.transactionsList.setGeometry(QRect(510, 80, 270, 400))
        self.transactionsStaticLbl = QLabel(self.centralwidget)
        self.transactionsStaticLbl.setObjectName(u"transactionsStaticLbl")
        self.transactionsStaticLbl.setGeometry(QRect(510, 40, 121, 41))
        font3 = QFont()
        font3.setPointSize(15)
        self.transactionsStaticLbl.setFont(font3)
        self.depositBtn = QPushButton(self.centralwidget)
        self.depositBtn.setObjectName(u"depositBtn")
        self.depositBtn.setGeometry(QRect(40, 120, 331, 51))
        self.depositBtn.setFont(font3)
        self.accountLbl = QLabel(self.centralwidget)
        self.accountLbl.setObjectName(u"accountLbl")
        self.accountLbl.setGeometry(QRect(260, 430, 151, 41))
        self.accountLbl.setFont(font1)
        self.routingStaticLbl = QLabel(self.centralwidget)
        self.routingStaticLbl.setObjectName(u"routingStaticLbl")
        self.routingStaticLbl.setGeometry(QRect(40, 470, 211, 41))
        self.routingStaticLbl.setFont(font1)
        self.routingLbl = QLabel(self.centralwidget)
        self.routingLbl.setObjectName(u"routingLbl")
        self.routingLbl.setGeometry(QRect(260, 470, 151, 41))
        self.routingLbl.setFont(font1)
        self.withdrawBtn = QPushButton(self.centralwidget)
        self.withdrawBtn.setObjectName(u"withdrawBtn")
        self.withdrawBtn.setGeometry(QRect(40, 190, 331, 51))
        self.withdrawBtn.setFont(font3)
        self.transferBtn = QPushButton(self.centralwidget)
        self.transferBtn.setObjectName(u"transferBtn")
        self.transferBtn.setGeometry(QRect(40, 260, 331, 51))
        self.transferBtn.setFont(font3)
        self.manageCardBtn = QPushButton(self.centralwidget)
        self.manageCardBtn.setObjectName(u"manageCardBtn")
        self.manageCardBtn.setGeometry(QRect(40, 330, 331, 51))
        self.manageCardBtn.setFont(font3)
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self, self):
        self.setWindowTitle(QCoreApplication.translate("self", u"Bank of Oakland: <Account Number>", None))
        self.balanceStaticLbl.setText(QCoreApplication.translate("self", u"Balance:", None))
        self.balanceLbl.setText(QCoreApplication.translate("self", u"X,XXX,XXX", None))
        self.accountStaticLbl.setText(QCoreApplication.translate("self", u"Account Number:", None))
        self.accountInfoLbl.setText(QCoreApplication.translate("self", u"<Card name> <Account Holder Name>", None))
        self.transactionsStaticLbl.setText(QCoreApplication.translate("self", u"Transactions:", None))
        self.depositBtn.setText(QCoreApplication.translate("self", u"Deposit", None))
        self.accountLbl.setText(QCoreApplication.translate("self", u"XXXXXXXXX", None))
        self.routingStaticLbl.setText(QCoreApplication.translate("self", u"Routing Number:", None))
        self.routingLbl.setText(QCoreApplication.translate("self", u"XXXXXXXXX", None))
        self.withdrawBtn.setText(QCoreApplication.translate("self", u"Withdraw", None))
        self.transferBtn.setText(QCoreApplication.translate("self", u"Transfer", None))
        self.manageCardBtn.setText(QCoreApplication.translate("self", u"Manage Card", None))
    # retranslateUi

"""