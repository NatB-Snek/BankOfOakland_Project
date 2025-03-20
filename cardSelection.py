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
        self.font = QFont()

        self.addBtn = QPushButton("New Card", self)
        self.titleLbl = QLabel("Bank of Oakland \nB O O",self)
        self.lbl2 = QLabel("Cards in the name of: " + "<User Name>",self)


    #List
        self.numberOfCards = 5 #SQL STATEMENT NEEDED

        self.formLayout = QFormLayout()
        self.groupBox = QGroupBox("Accounts:")
            
        self.groupBox.setLayout(self.formLayout)
        self.scroll = QScrollArea(self)
        self.layout = QVBoxLayout(self)

        self.initUI()

    def initUI(self):
        self.addBtn.setGeometry(140, 480, 121, 31)
        self.titleLbl.setGeometry(106, 20, 191, 51)
        self.font.setPointSize(16)
        self.titleLbl.setFont(self.font)
        self.titleLbl.setLayoutDirection(Qt.LeftToRight)
        self.titleLbl.setAlignment(Qt.AlignCenter)
        self.titleLbl.setStyleSheet("font-weight: bold;")
        self.lbl2.setGeometry(50, 85, 300, 21)
        self.font.setPointSize(11)
        self.lbl2.setFont(self.font)

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

              buttonList.append(QPushButton("", self))
              currentButton = buttonList[i]
              currentButton.setText("Make these buttons functional")

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