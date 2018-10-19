# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\xzhao\OneDrive\v2rayM\client\SysUI\ProjectItemWidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ProjectItemWidget(object):
    def setupUi(self, ProjectItemWidget):
        ProjectItemWidget.setObjectName("ProjectItemWidget")
        ProjectItemWidget.resize(340, 75)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ProjectItemWidget.sizePolicy().hasHeightForWidth())
        ProjectItemWidget.setSizePolicy(sizePolicy)
        ProjectItemWidget.setAlignment(QtCore.Qt.AlignCenter)
        self.horizontalLayout = QtWidgets.QVBoxLayout(ProjectItemWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widgetBottom = QtWidgets.QWidget(ProjectItemWidget)
        self.widgetBottom.setObjectName("widgetBottom")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widgetBottom)
        self.verticalLayout.setContentsMargins(20, 18, 20, 18)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelName = QtWidgets.QLabel(self.widgetBottom)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelName.sizePolicy().hasHeightForWidth())
        self.labelName.setSizePolicy(sizePolicy)
        self.labelName.setText("")
        self.labelName.setObjectName("labelName")
        self.verticalLayout.addWidget(self.labelName)
        self.labelTime = QtWidgets.QLabel(self.widgetBottom)
        self.labelTime.setText("")
        self.labelTime.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelTime.setObjectName("labelTime")
        self.verticalLayout.addWidget(self.labelTime)
        self.horizontalLayout.addWidget(self.widgetBottom)

        self.retranslateUi(ProjectItemWidget)
        QtCore.QMetaObject.connectSlotsByName(ProjectItemWidget)

    def retranslateUi(self, ProjectItemWidget):
        _translate = QtCore.QCoreApplication.translate
        ProjectItemWidget.setWindowTitle(_translate("ProjectItemWidget", "ProjectItemWidget"))
        ProjectItemWidget.setText(_translate("ProjectItemWidget", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ProjectItemWidget = QtWidgets.QLabel()
    ui = Ui_ProjectItemWidget()
    ui.setupUi(ProjectItemWidget)
    ProjectItemWidget.show()
    sys.exit(app.exec_())

