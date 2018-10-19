from SysUI.MainWindow_UI import Ui_MainWindow
from SysUI.ProjectItemWidget_UI import Ui_ProjectItemWidget
from CoreInclude.ProjectWidget import ProjectItemWidget, SortFilterProxyModel
from CoreInclude import Config
from CoreInclude import CoreLogic
from CoreInclude.MessageBox import MessageDialog
from TitleMain import TitleWidget
import sys
import json
from CoreInclude.SystemTray import TrayIcon
# from demo import Ui_MainWindow
from PyQt5 import QtCore

# from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import (QMainWindow, QHBoxLayout, QMessageBox,
                             QApplication, QGraphicsPixmapItem, QGraphicsScene,
                             QMenu, QAction, QButtonGroup, QLabel, QSpacerItem,
                             QSizePolicy)
# from PyQt5.QtGui import QPalette, QColor, QCursor
from PyQt5.QtGui import QPainter, QIcon, QTextCursor

from PyQt5.QtGui import QStandardItemModel, QStandardItem

from PyQt5.QtGui import QFontDatabase

# from Utils.SortFilterProxyModel import SortFilterProxyModel

from PyQt5.QtCore import Qt, pyqtSlot

# from PyQt5 import uic
# 加载资源文件
# import main
# import qss


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.OthersetupUI()  # 窗口设置

        # 加载QSS
        self.setStyleSheet(Config.QSS())

        # 重定向输出
        # sys.stdout = EmittingStream(textWritten=self.OutputWritten)
        # sys.stderr = EmittingStream(textWritten=self.OutputWritten)

    # 窗口定义
    def OthersetupUI(self):
        # 设置托盘
        self.sysTray = TrayIcon(self)
        self.sysTray.show()
        # 设置标题
        self.setWindowTitle(Config.TitleName)
        self.setWindowIcon(QIcon('source/img/main.ico'))
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)  # 禁止最大化
        if sys.platform == 'win32':
            self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)  # 隐藏标题栏
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
            self.setFixedSize(self.width(), self.height())  # 固定尺寸
        else:
            self.setFixedSize(self.width(), self.height() - 40)
        self.set_titlebar()
        self.set_projectui()
        self.order_int()
        # 默认隐藏滚动条
        self.rightScrollBar.setVisible(False)

        # self.cmd_output.setReadOnly(True)  # 设置控制台只读

    def set_titlebar(self):
        # 在菜单中添加自定义的标题栏
        layout = QHBoxLayout(self.menubar, spacing=0)
        layout.setContentsMargins(0, 0, 0, 0)
        self.titleWidget = TitleWidget(self)
        # mac及linux下使用系统状态栏
        if sys.platform == 'win32':
            self.titleWidget.labelTitle.setText(Config.TitleName)
            self.titleWidget.windowMoved.connect(self.doMoveWindow)
            self.titleWidget.buttonMin.clicked.connect(self.hide)
            self.titleWidget.buttonClose.clicked.connect(self.quit)
        layout.addWidget(self.titleWidget)

    def doMoveWindow(self, pos):
        if self.isMaximized() or self.isFullScreen():
            return
        # 移动窗口
        self.move(self.x() + pos.x(), self.y() + pos.y())

    # 功能绑定
    def MainEvent(self):
        self.testbutton.clicked.connect(self.msg)
        # self.loginbutton.clicked.connect(lambda: self.click_login())
        # pass

    def set_projectui(self):
        self.listViewProjects.setVerticalScrollBar(self.rightScrollBar)
        self.horizontalLayout.addWidget(self.rightScrollBar)
        self.projectModel = QStandardItemModel(self.listViewProjects)
        self.filterProjectModel = SortFilterProxyModel(self.listViewProjects)
        self.filterProjectModel.setSourceModel(self.projectModel)
        self.listViewProjects.setModel(self.filterProjectModel)

    def set_Projects(self, order_index):
        order_information = Config.get_client()
        tmp_data = {
            'username': Config.get_username(),
            'orderid': order_information[order_index]['orderid'],
            'serverid': order_information[order_index]['serverid'],
        }
        CoreLogic.connect_message(tmp_data)
        print(Config.get_order())
        if order_information[order_index]['status'] != 'Active':
            servers = []
        else:
            servers = CoreLogic.get_server()
        self.projectModel.clear()
        self.rightScrollBar.setVisible(False)
        if servers == []:
            MessageDialog.error(
                self, self.windowTitle(), '当前选中订单' +
                order_information[order_index]['name'] + '无效，\n请更换订单尝试！')
            return
        for i, server in servers:
            try:
                project = server
                item = QStandardItem('    {}'.format(server[0]))
                self.projectModel.appendRow(item)
                index = self.filterProjectModel.mapFromSource(item.index())
                widget = ProjectItemWidget(project, self.listViewProjects)
                item.setSizeHint(widget.size())
                self.listViewProjects.setIndexWidget(index, widget)
                if i == 0:
                    self.listViewProjects.setCurrentIndex(index)  # 默认选中
                elif i > 5:
                    self.rightScrollBar.setVisible(True)
                    self.tmp.setMaximumSize(QtCore.QSize(1, 0))
            except Exception as e:
                CoreLogic.Call_Error(e)
                continue

    # 控制台输出
    def OutputWritten(self, text):
        cursor = self.cmd_output.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
        self.cmd_output.setTextCursor(cursor)
        self.cmd_output.ensureCursorVisible()

    # 退出警告
    def quit(self):
        reply = MessageDialog.question(self, self.windowTitle(), '你确认要退出吗？')
        if reply == 1:
            self.close()
            self.sysTray.setVisible(False)
            sys.exit(1)
        elif reply == 0:
            pass

    # @pyqtignal()
    def order_int(self):
        order_list = Config.get_client()
        order_dict = {}
        for i, order in enumerate(order_list):
            self.comboBox.addItem("")
            self.comboBox.setItemText(i, order['name'])
            order_dict[i] = order['name']
        self.comboBox.activated[int].connect(self.get_order)
        self.get_order(0)

    def get_order(self, order_index):
        self.set_Projects(order_index)

    # 功能定义
    def open_login(self):
        sys.exit(1)

    def msg(self):
        print('test button clicked.')


class EmittingStream(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str)

    def write(self, text):
        self.textWritten.emit(str(text))
