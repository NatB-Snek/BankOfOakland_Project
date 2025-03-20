import sys, os
from PyQt5.QtWidgets import *
##Libraries used##: QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QLineEdit, QSizePolicy, QWidget
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bank of Oakland: Account Creation")
        self.setFixedSize(400, 550) #(x, y, width, height)
        self.setWindowIcon(QIcon("placeholder.jpg")) #File must be in the same directory

        self.numberOfCards = 5 #SQL STATEMENT NEEDED

        self.formLayout = QFormLayout()
        self.groupBox = QGroupBox("Accounts:")
            
        self.groupBox.setLayout(self.formLayout)
        self.scroll = QScrollArea(self)
        self.layout = QVBoxLayout(self)

        self.initUI()

    def initUI(self):
        self.formLayout.setVerticalSpacing(30)
        self.scroll.setWidget(self.groupBox)
        self.scroll.setWidgetResizable(True)
        self.scroll.setGeometry(50, 110, 300, 350)
        #self.layout.addWidget(self.scroll)

        checkboxList = []
        labelList = []
        buttonList = []

        #Fun SQL stuff gonna happen here
        for i in range(self.numberOfCards):
              checkboxList.append(QCheckBox(""))

              buttonList.append(QPushButton(""))
              currentButton = buttonList[i]
              currentButton.setText("Hello")
              currentButton.setHight(1000)

              self.formLayout.addRow(currentButton)
    
    def buttonClicked():
          pass
    
    def addClick():
          pass

    
    


def main():
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())

if __name__ == "__main__":
        main()