#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication
from Login import LoginWindow


def login_ui():
    app = QApplication(sys.argv)
    dialog = LoginWindow()
    dialog.exec_()
    sys.exit(app.exec_())


if __name__ == '__main__':
    login_ui()
