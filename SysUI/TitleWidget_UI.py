# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\xzhao\OneDrive\v2rayM\client\SysUI\TitleWidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TitleWidget(object):
    def setupUi(self, TitleWidget):
        TitleWidget.setObjectName("TitleWidget")
        TitleWidget.resize(496, 34)
        TitleWidget.setMinimumSize(QtCore.QSize(0, 34))
        TitleWidget.setMaximumSize(QtCore.QSize(16777215, 34))
        self.horizontalLayout = QtWidgets.QHBoxLayout(TitleWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.labelTitle = QtWidgets.QLabel(TitleWidget)
        self.labelTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitle.setObjectName("labelTitle")
        self.horizontalLayout.addWidget(self.labelTitle)
        spacerItem1 = QtWidgets.QSpacerItem(32, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(3, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.buttonMin = QtWidgets.QPushButton(TitleWidget)
        self.buttonMin.setMinimumSize(QtCore.QSize(34, 34))
        self.buttonMin.setMaximumSize(QtCore.QSize(34, 34))
        self.buttonMin.setObjectName("buttonMin")
        self.horizontalLayout.addWidget(self.buttonMin)
        self.buttonClose = QtWidgets.QPushButton(TitleWidget)
        self.buttonClose.setMinimumSize(QtCore.QSize(34, 34))
        self.buttonClose.setMaximumSize(QtCore.QSize(34, 34))
        self.buttonClose.setObjectName("buttonClose")
        self.horizontalLayout.addWidget(self.buttonClose)

        self.retranslateUi(TitleWidget)
        QtCore.QMetaObject.connectSlotsByName(TitleWidget)

    def retranslateUi(self, TitleWidget):
        _translate = QtCore.QCoreApplication.translate
        TitleWidget.setWindowTitle(_translate("TitleWidget", "TitleWidget"))
        self.labelTitle.setText(_translate("TitleWidget", "title"))
        self.buttonMin.setText(_translate("TitleWidget", "0"))
        self.buttonClose.setText(_translate("TitleWidget", "r"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TitleWidget = QtWidgets.QWidget()
    ui = Ui_TitleWidget()
    ui.setupUi(TitleWidget)
    TitleWidget.show()
    sys.exit(app.exec_())

