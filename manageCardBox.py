### !!!NOTE!!! ###
#None of this actually works yet, needs to be formated

class Ui_self(object):
    def setupUi(self, self):
        if self.objectName():
            self.setObjectName(u"self")
        self.resize(254, 247)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lockBtn = QPushButton(self.centralwidget)
        self.lockBtn.setObjectName(u"lockBtn")
        self.lockBtn.setGeometry(QRect(20, 100, 141, 23))
        self.unlockCkBx = QCheckBox(self.centralwidget)
        self.unlockCkBx.setObjectName(u"unlockCkBx")
        self.unlockCkBx.setGeometry(QRect(130, 180, 111, 61))
        self.deleteBtn = QPushButton(self.centralwidget)
        self.deleteBtn.setObjectName(u"deleteBtn")
        self.deleteBtn.setGeometry(QRect(20, 140, 141, 23))
        self.okBtn = QPushButton(self.centralwidget)
        self.okBtn.setObjectName(u"okBtn")
        self.okBtn.setGeometry(QRect(40, 200, 75, 23))
        self.renameBtn = QPushButton(self.centralwidget)
        self.renameBtn.setObjectName(u"renameBtn")
        self.renameBtn.setGeometry(QRect(20, 20, 75, 23))
        self.renameInputReciever = QLineEdit(self.centralwidget)
        self.renameInputReciever.setObjectName(u"renameInputReciever")
        self.renameInputReciever.setGeometry(QRect(120, 20, 113, 20))
        self.cleanBtn = QPushButton(self.centralwidget)
        self.cleanBtn.setObjectName(u"cleanBtn")
        self.cleanBtn.setGeometry(QRect(20, 60, 141, 23))
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self, self):
        self.setWindowTitle(QCoreApplication.translate("self", u"Manage Card", None))
        self.lockBtn.setText(QCoreApplication.translate("self", u"Lock Card", None))
        self.unlockCkBx.setText(QCoreApplication.translate("self", u"Unlock Options", None))
        self.deleteBtn.setText(QCoreApplication.translate("self", u"Delete Card", None))
        self.okBtn.setText(QCoreApplication.translate("self", u"Ok", None))
        self.renameBtn.setText(QCoreApplication.translate("self", u"Rename", None))
        self.cleanBtn.setText(QCoreApplication.translate("self", u"Clean History", None))
    # retranslateUi

