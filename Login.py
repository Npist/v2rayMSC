#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import Main
import sys
from CoreInclude import Config
from CoreInclude import CoreLogic
from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
from SysUI.LoginDialog_UI import Ui_LoginDialog


class LoginWindow(QDialog, Ui_LoginDialog):
    def __init__(self, *args, **kwargs):
        super(LoginWindow, self).__init__()
        self.setupUi(self)

        # 杂乱设置
        self.setWindowIcon(QIcon('source/img/main.ico'))  # 设置图标
        self.setWindowFlags(Qt.CustomizeWindowHint)  # 隐藏标题栏
        self.setWindowFlags(Qt.FramelessWindowHint)  # 隐藏边框
        # 设置边框
        self.dialogWidgetBg.setContentsMargins(1, 1, 1, 1)
        self.BorderWidget = self.dialogWidgetBg
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint)
        # 设置本地化文字
        self.labelHead.setPixmap(QPixmap("source/img/logo_193x80.png"))
        self.editUsername.setPlaceholderText("邮箱")
        self.editPassword.setPlaceholderText("密码")

        # 加载QSS
        self.setStyleSheet(Config.QSS())

        # 按键功能
        self.MainEvent()

    # 按键绑定
    def MainEvent(self):
        self.widgetTitle.buttonClose.clicked.connect(self.quit)
        self.widgetTitle.windowMoved.connect(self.doMoveWindow)
        self.buttonLogin.clicked.connect(self.click_login)

    def doMoveWindow(self, pos):
        if self.isMaximized() or self.isFullScreen():
            return
        self.move(self.x() + pos.x(), self.y() + pos.y())

    def click_login(self):
        windowList = []
        user = self.editUsername.text().strip()
        passwd = self.editPassword.text().strip()
        if user == '' or passwd == '':
            self.labelNotice.setText(self.tr('邮箱或密码不能为空'))
        else:
            data = {
                'username': user,
                'password': passwd,
            }
            CoreLogic.user_login(data)
            login_bool = CoreLogic.login_check()
            if login_bool is False:
                self.labelNotice.setText(self.tr('邮箱或密码错误！请检查后再试'))
            else:
                Config.set_username = user
                main_window = Main.MainWindow()
                windowList.append(main_window)
                main_window.show()
                self.close()

    def quit(self):
        self.close()
        sys.exit(1)
