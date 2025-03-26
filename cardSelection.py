import sys, os
from PyQt5.QtWidgets import *
##Libraries used##: QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QLineEdit, QSizePolicy, QWidget
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

from main import MainWindow

class cardSelection(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bank of Oakland: Card Selection")
        self.setFixedSize(400, 550)
        self.setWindowIcon(QIcon("placeholder.jpg"))
        self.font = QFont()

        username = "Temp"

        self.addBtn = QPushButton("New Card", self)
        self.titleLbl = QLabel("Bank of Oakland \nB O O", self)
        self.lbl2 = QLabel("Cards in the name of: " + str(username), self)

        self.numberOfCards = 3  # Placeholder for SQL integration

        self.formLayout = QFormLayout()
        self.groupBox = QGroupBox("Accounts:")
        self.scroll = QScrollArea(self)
        self.layout = QVBoxLayout(self)

        self.initUI()

    def initUI(self):
        self.groupBox.setLayout(self.formLayout)
        
        self.scroll.setWidget(self.groupBox)
        self.scroll.setWidgetResizable(True)
        self.scroll.setGeometry(50, 110, 300, 350)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.addBtn.setGeometry(140, 480, 121, 31)
        self.addBtn.clicked.connect(self.addClicked) #This adds a new card
        
        self.titleLbl.setGeometry(106, 20, 191, 51)
        self.font.setPointSize(16)
        self.titleLbl.setFont(self.font)
        self.titleLbl.setAlignment(Qt.AlignCenter)
        self.titleLbl.setStyleSheet("font-weight: bold;")
        self.lbl2.setGeometry(50, 85, 300, 21)
        self.font.setPointSize(11)
        self.lbl2.setFont(self.font)

        self.formLayout.setVerticalSpacing(15)

        for i in range(self.numberOfCards):
            self.addCardRow()
            

    def addCardRow(self):
        # Information gathering:
        # def addCardRow(self, i):
        # i will be what row we will be gathering information from, temp values for now
        balance = 100
        cardNumber = 1000


        balanceLabel = QLabel("Balance: ")
        balanceAmount = QLabel("$ " + str(balance))  # Placeholder
        cardButton = QPushButton("**** " + str(cardNumber))  # Placeholder for last 4 digits
        cardButton.setFixedHeight(40)
        cardButton.setFixedWidth(100)
        cardButton.clicked.connect(lambda: self.openMainWindow())

        font = QFont()
        font.setPointSize(10)  # Example: Arial, size 12, bold
        balanceLabel.setFont(font)
        balanceAmount.setFont(font)
        cardButton.setFont(font)
        
        rowLayout = QHBoxLayout()
        rowLayout.addWidget(balanceLabel)
        rowLayout.addWidget(balanceAmount)
        rowLayout.addStretch()
        rowLayout.addWidget(cardButton)
            
        self.formLayout.addRow(rowLayout)

        # Refresh UI
        self.groupBox.adjustSize()
        self.scroll.setWidget(self.groupBox)
        self.repaint()

    def addClicked(self):
        self.openAddCardDialog()
        
    def openMainWindow(self):
        self.mainWindow = MainWindow()  # Open main window with details
        self.mainWindow.show()

    def openAddCardDialog(self):
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
        
        confirmButton.clicked.connect(lambda: self.confirmAddCard(dialog))
        cancelButton.clicked.connect(dialog.reject)
        dialog.exec_()

    def confirmAddCard(self, dialog):
            dialog.accept()
            self.addCardRow()

def main():
    app = QApplication(sys.argv)
    window = cardSelection()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
