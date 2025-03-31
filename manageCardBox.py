import sys, os
from PyQt5.QtWidgets import *
##Libraries used##: QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QLineEdit, QSizePolicy
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Manage Card")
        self.setFixedSize(250, 250)
        self.setWindowIcon(QIcon("placeholder.jpg"))

        # Declare UI elements
        self.lockBtn = QPushButton("Lock Card", self)
        self.unlockCkBx = QCheckBox("Unlock Options", self)
        self.deleteBtn = QPushButton("Delete Card", self)
        self.okBtn = QPushButton("Ok", self)
        self.cleanBtn = QPushButton("Clean History", self)

        self.initUi()

        # Initial lock state
        self.lockBtn.setEnabled(False)
        self.deleteBtn.setEnabled(False)

        # Connections
        self.unlockCkBx.stateChanged.connect(self.toggle_lock_delete)
        self.lockBtn.clicked.connect(self.lock_card)
        self.deleteBtn.clicked.connect(self.delete_card)
        self.cleanBtn.clicked.connect(self.clean_history)
        self.okBtn.clicked.connect(self.close)

    def initUi(self):
        self.lockBtn.setGeometry(20, 100, 141, 23)
        self.unlockCkBx.setGeometry(130, 180, 111, 61)
        self.deleteBtn.setGeometry(20, 140, 141, 23)
        self.okBtn.setGeometry(40, 200, 75, 23)
        self.cleanBtn.setGeometry(20, 60, 141, 23)

    def toggle_lock_delete(self, state):
        enabled = state == Qt.Checked
        self.lockBtn.setEnabled(enabled)
        self.deleteBtn.setEnabled(enabled)

    def lock_card(self):
        QMessageBox.information(self, "Card Locked", "This card is now locked.")
        if self.parent():
            self.parent().depositBtn.setEnabled(False)
            self.parent().withdrawBtn.setEnabled(False)
            self.parent().transferBtn.setEnabled(False)

    def clean_history(self):
        if self.parent():
            self.parent().transactionsList.clear()
            QMessageBox.information(self, "History Cleared", "Transaction history has been cleared.")

    def delete_card(self):
        if self.parent() and hasattr(self.parent(), 'balance'):
            balance = self.parent().balance
            if balance > 0:
                has_other_account = True  # Simulated condition
                if has_other_account:
                    choice = QMessageBox.question(
                        self,
                        "Transfer Funds?",
                        "This card still has a balance. Would you like to transfer the remaining funds to another account before deletion?",
                        QMessageBox.Yes | QMessageBox.No,
                        QMessageBox.No
                    )
                    if choice == QMessageBox.Yes:
                        self.parent().balance = 0
                        self.parent().update_balance_display()
                        self.parent().transactionsList.addItem("Transferred remaining balance to another account")
                        QMessageBox.information(self, "Success", "Funds transferred. You may now delete the card.")
                    else:
                        QMessageBox.warning(self, "Cancelled", "Card cannot be deleted while balance remains.")
                        return
                else:
                    QMessageBox.critical(self, "Cannot Delete", "Card has a balance and no other account exists to transfer to.")
                    return

        QMessageBox.information(self, "Card Deleted", "Card has been successfully deleted.")
        self.parent().close()
        self.close()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
