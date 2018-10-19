#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Forked from :https://github.com/892768447/QtSkin
"""
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog
from SysUI.MessageDialog_UI import Ui_MessageDialog
from CoreInclude import Config


class MessageDialog(QDialog, Ui_MessageDialog):
    def __init__(self, *args, title='', message='', **kwargs):
        super(MessageDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setStyleSheet(Config.QSS())  # 加载QSS
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint)

        self.setTitle(title).setMessage(message)

        self.widgetTitle.windowMoved.connect(self.doMoveWindow)
        self.widgetTitle.buttonClose.clicked.connect(self.reject)

    def showCancelButton(self, show=True):
        self.buttonCancel.setVisible(show)

    def setTitle(self, title):
        self.widgetTitle.setTitle(title)
        return self

    def setMessage(self, message):
        self.labelMessage.setText(message)
        return self

    def close(self):
        super(MessageDialog, self).close()
        self.deleteLater()

    def doMoveWindow(self, pos):
        if self.isMaximized() or self.isFullScreen():
            return
        # 移动窗口
        self.move(self.x() + pos.x(), self.y() + pos.y())

    @classmethod
    def information(cls, parent=None, title='', message=''):
        dialog = MessageDialog(parent, title=title, message=message)
        dialog.showCancelButton(False)
        ret = dialog.exec_()
        dialog.close()
        return ret

    @classmethod
    def error(cls, parent=None, title='', message=''):
        dialog = MessageDialog(parent, title=title, message=message)
        dialog.setProperty('active', 'error')
        dialog.showCancelButton(False)
        ret = dialog.exec_()
        dialog.close()
        return ret

    @classmethod
    def question(cls, parent=None, title='', message=''):
        dialog = MessageDialog(parent, title=title, message=message)
        ret = dialog.exec_()
        dialog.close()
        return ret
