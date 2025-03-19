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
        
                self.centralwidget = QWidget(self)
                self.userEntry = QTextEdit(self.centralwidget)
                self.passEntry = QTextEdit(self.centralwidget)
                self.createBtn = QPushButton(self.centralwidget)
                self.userLbl = QLabel(self.centralwidget)
                self.firstEntry = QTextEdit(self.centralwidget)
                self.lastEntry = QTextEdit(self.centralwidget)
                self.birthEntry = QTextEdit(self.centralwidget)
                self.checkBox = QCheckBox(self.centralwidget)
                self.cancelBtn = QPushButton(self.centralwidget)
                self.passLbl = QLabel(self.centralwidget)
                self.firstLbl = QLabel(self.centralwidget)
                self.birthLbl = QLabel(self.centralwidget)
                self.emailLbl = QLabel(self.centralwidget)
                self.label = QLabel(self.centralwidget)
                self.titleLbl = QLabel(self.centralwidget)
                self.emailEntry = QTextEdit(self.centralwidget)
                self.lastLbl = QLabel(self.centralwidget)
                self.setCentralWidget(self.centralwidget)

                self.initUI()

        def initUI(self):
                self.userEntry.setGeometry(160, 60, 201, 41)
                self.passEntry.setGeometry(160, 120, 201, 41)
                self.createBtn.setGeometry(20, 440, 121, 31)
                self.userLbl.setGeometry(20, 60, 111, 41)
                self.userLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
                self.firstEntry.setGeometry(160, 180, 201, 41)
                self.lastEntry.setGeometry(160, 240, 201, 41)
                self.birthEntry.setGeometry(160, 300, 201, 41)
                self.checkBox.setGeometry(160, 440, 111, 31)
                self.cancelBtn.setGeometry(20, 490, 121, 31)
                self.passLbl.setGeometry(20, 120, 111, 41)
                self.passLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
                self.firstLbl.setGeometry(20, 180, 111, 41)
                self.firstLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
                self.birthLbl.setGeometry(20, 300, 111, 41)
                self.birthLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
                self.emailLbl.setGeometry(20, 360, 111, 41)
                self.emailLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
                self.label.setGeometry(160, 490, 91, 21)
                self.titleLbl.setGeometry(126, 20, 141, 20)
                self.titleLbl.setAlignment(Qt.AlignCenter)
                self.emailEntry.setGeometry(160, 360, 201, 41)
                self.lastLbl.setGeometry(20, 240, 111, 41)
                self.lastLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

                

def main():
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())

if __name__ == "__main__":
        main()
        