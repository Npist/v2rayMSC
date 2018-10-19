#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtCore import pyqtSignal, QPoint, Qt
from PyQt5.QtWidgets import QWidget

from SysUI.TitleWidget_UI import Ui_TitleWidget

# from Widgets.Dialogs.LoginDialog import LoginDialog


class TitleWidget(QWidget, Ui_TitleWidget):

    windowMoved = pyqtSignal(QPoint)

    def __init__(self, *args, **kwargs):
        super(TitleWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.prePos = None

    def mousePressEvent(self, event):
        super(TitleWidget, self).mousePressEvent(event)
        if event.button() == Qt.LeftButton:
            self.prePos = event.pos()

    def mouseReleaseEvent(self, event):
        super(TitleWidget, self).mouseReleaseEvent(event)
        self.prePos = None

    def mouseMoveEvent(self, event):
        super(TitleWidget, self).mouseMoveEvent(event)
        if not self.prePos:
            return
        pos = event.pos() - self.prePos
        self.windowMoved.emit(pos)
