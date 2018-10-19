# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\xzhao\OneDrive\v2rayM\client\SysUI\TitleOtherWidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BaseTitleWidget(object):
    def setupUi(self, BaseTitleWidget):
        BaseTitleWidget.setObjectName("BaseTitleWidget")
        BaseTitleWidget.resize(375, 28)
        BaseTitleWidget.setMinimumSize(QtCore.QSize(0, 28))
        BaseTitleWidget.setMaximumSize(QtCore.QSize(16777215, 28))
        self.horizontalLayout = QtWidgets.QHBoxLayout(BaseTitleWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelIcon = QtWidgets.QLabel(BaseTitleWidget)
        self.labelIcon.setMinimumSize(QtCore.QSize(28, 0))
        self.labelIcon.setMaximumSize(QtCore.QSize(28, 16777215))
        self.labelIcon.setText("")
        self.labelIcon.setAlignment(QtCore.Qt.AlignCenter)
        self.labelIcon.setObjectName("labelIcon")
        self.horizontalLayout.addWidget(self.labelIcon)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.labelTitle = QtWidgets.QLabel(BaseTitleWidget)
        self.labelTitle.setText("")
        self.labelTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitle.setObjectName("labelTitle")
        self.horizontalLayout.addWidget(self.labelTitle)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.buttonClose = QtWidgets.QPushButton(BaseTitleWidget)
        self.buttonClose.setMinimumSize(QtCore.QSize(28, 28))
        self.buttonClose.setMaximumSize(QtCore.QSize(28, 28))
        self.buttonClose.setObjectName("buttonClose")
        self.horizontalLayout.addWidget(self.buttonClose)

        self.retranslateUi(BaseTitleWidget)
        QtCore.QMetaObject.connectSlotsByName(BaseTitleWidget)

    def retranslateUi(self, BaseTitleWidget):
        _translate = QtCore.QCoreApplication.translate
        BaseTitleWidget.setWindowTitle(_translate("BaseTitleWidget", "BaseTitleWidget"))
        self.buttonClose.setText(_translate("BaseTitleWidget", "r"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BaseTitleWidget = QtWidgets.QWidget()
    ui = Ui_BaseTitleWidget()
    ui.setupUi(BaseTitleWidget)
    BaseTitleWidget.show()
    sys.exit(app.exec_())

