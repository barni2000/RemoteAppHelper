#!/usr/bin/env python3
from PyQt5.QtWidgets import QApplication
from app import ApplicationDialog
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = ApplicationDialog()
    w.show()

    app.exec()
