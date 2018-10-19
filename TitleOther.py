#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtCore import pyqtSignal, QPoint, Qt
from PyQt5.QtWidgets import QWidget

from SysUI.TitleOtherWidget_UI import Ui_BaseTitleWidget


class BaseTitleWidget(QWidget, Ui_BaseTitleWidget):

    windowMoved = pyqtSignal(QPoint)

    # windowClosed = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(BaseTitleWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setAttribute(Qt.WA_StyledBackground, True)

    def setTitle(self, title):
        self.labelTitle.setText(title)

    def mousePressEvent(self, event):
        super(BaseTitleWidget, self).mousePressEvent(event)
        if event.button() == Qt.LeftButton:
            self.prePos = event.pos()

    def mouseReleaseEvent(self, event):
        super(BaseTitleWidget, self).mouseReleaseEvent(event)
        self.prePos = None

    def mouseMoveEvent(self, event):
        super(BaseTitleWidget, self).mouseMoveEvent(event)
        if not self.prePos:
            return
        pos = event.pos() - self.prePos
        self.windowMoved.emit(pos)
