from ui_login_dialog import Ui_LoginDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget
import keyring
import sys
import subprocess


class ApplicationDialog(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_LoginDialog()
        self.ui.setupUi(self)
        self.ui.pushButton_login.clicked.connect(self.run_app)
        self.ui.lineEdit_username.textChanged.connect(self.try_keyring)
        self.service_name = 'remoteapp_helper'

    @pyqtSlot()
    def run_app(self):
        password = self.ui.lineEdit_password.text()
        username = self.ui.lineEdit_username.text()
        keyring.set_password(self.service_name, username, password)
        subprocess.run([
            "xfreerdp", sys.argv[1],
            "/u:"+username,
            "/p:"+password,
            "/d:"+self.ui.lineEdit_domain.text()
        ])

    @pyqtSlot(str)
    def try_keyring(self, text):
        password = keyring.get_password(self.service_name, text)
        if password is not None:
            self.ui.lineEdit_password.setText(password)
