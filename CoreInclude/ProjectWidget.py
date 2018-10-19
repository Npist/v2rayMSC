from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt, QSortFilterProxyModel, pyqtSignal
from PyQt5.QtGui import QPainter, QStandardItem
from SysUI.ProjectItemWidget_UI import Ui_ProjectItemWidget


# 排序
class SortFilterProxyModel(QSortFilterProxyModel):
    def lessThan(self, source_left, source_right):
        if not source_left.isValid() or not source_right.isValid():
            return False
        # 获取数据
        leftData = self.sourceModel().data(source_left)
        rightData = self.sourceModel().data(source_right)
        if self.sortOrder() == Qt.AscendingOrder:
            leftData = leftData.split('-')[0]
            rightData = rightData.split('-')[0]
            return leftData < rightData
        return super(SortFilterProxyModel, self).lessThan(
            source_left, source_right)


# 功能
class ProjectItemWidget(QLabel, Ui_ProjectItemWidget):

    itemDeleted = pyqtSignal(QStandardItem)

    def __init__(self, project, *args, **kwargs):
        super(ProjectItemWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self._project = project
        self.setName(project[0])
        self.setTime(project[1])

    @property
    def project(self):
        return self._project

    def setName(self, name):
        self.labelName.setText(name)
        return self

    def setTime(self, time):
        self.labelTime.setText(time)
        return self

    def showEmpty(self, show=True):
        self.labelEmpty.setVisible(show)
        return self

    def paintEvent(self, event):
        super(ProjectItemWidget, self).paintEvent(event)
        pixmap = self.pixmap()
        if not pixmap or pixmap.isNull():
            # 虚线边框
            painter = QPainter(self)
            pen = painter.pen()
            pen.setStyle(Qt.DashLine)
            painter.setPen(pen)
            painter.drawRoundedRect(self.rect().adjusted(4, 4, -4, -4), 4, 4)
