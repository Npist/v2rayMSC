# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\xzhao\OneDrive\v2rayM\client\SysUI\MessageDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MessageDialog(object):
    def setupUi(self, MessageDialog):
        MessageDialog.setObjectName("MessageDialog")
        MessageDialog.resize(360, 129)
        MessageDialog.setMinimumSize(QtCore.QSize(360, 0))
        MessageDialog.setMaximumSize(QtCore.QSize(360, 16777215))
        self.horizontalLayout = QtWidgets.QHBoxLayout(MessageDialog)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dialogWidgetBg = QtWidgets.QWidget(MessageDialog)
        self.dialogWidgetBg.setObjectName("dialogWidgetBg")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dialogWidgetBg)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(18)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widgetTitle = BaseTitleWidget(self.dialogWidgetBg)
        self.widgetTitle.setMinimumSize(QtCore.QSize(0, 28))
        self.widgetTitle.setMaximumSize(QtCore.QSize(16777215, 28))
        self.widgetTitle.setObjectName("widgetTitle")
        self.verticalLayout.addWidget(self.widgetTitle)
        self.labelMessage = QtWidgets.QLabel(self.dialogWidgetBg)
        self.labelMessage.setText("")
        self.labelMessage.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMessage.setObjectName("labelMessage")
        self.verticalLayout.addWidget(self.labelMessage)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(15, -1, 15, 15)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.buttonCancel = QtWidgets.QPushButton(self.dialogWidgetBg)
        self.buttonCancel.setMinimumSize(QtCore.QSize(75, 25))
        self.buttonCancel.setMaximumSize(QtCore.QSize(75, 25))
        self.buttonCancel.setObjectName("buttonCancel")
        self.horizontalLayout_2.addWidget(self.buttonCancel)
        self.buttonOk = QtWidgets.QPushButton(self.dialogWidgetBg)
        self.buttonOk.setMinimumSize(QtCore.QSize(75, 25))
        self.buttonOk.setMaximumSize(QtCore.QSize(75, 25))
        self.buttonOk.setDefault(True)
        self.buttonOk.setObjectName("buttonOk")
        self.horizontalLayout_2.addWidget(self.buttonOk)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addWidget(self.dialogWidgetBg)

        self.retranslateUi(MessageDialog)
        self.buttonCancel.clicked.connect(MessageDialog.reject)
        self.buttonOk.clicked.connect(MessageDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(MessageDialog)

    def retranslateUi(self, MessageDialog):
        _translate = QtCore.QCoreApplication.translate
        MessageDialog.setWindowTitle(_translate("MessageDialog", "MessageDialog"))
        self.buttonCancel.setText(_translate("MessageDialog", "Cancel"))
        self.buttonOk.setText(_translate("MessageDialog", "Ok"))

from TitleOther import BaseTitleWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MessageDialog = QtWidgets.QDialog()
    ui = Ui_MessageDialog()
    ui.setupUi(MessageDialog)
    MessageDialog.show()
    sys.exit(app.exec_())

