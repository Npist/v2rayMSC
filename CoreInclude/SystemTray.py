from PyQt5.QtWidgets import QSystemTrayIcon, QMenu, QAction
from PyQt5.QtGui import QIcon


class TrayIcon(QSystemTrayIcon):
    def __init__(self, parent=None):
        super(TrayIcon, self).__init__(parent)
        self.showMenu()
        self.MainEvent()
        self.parentwindow = self.parent()

    def showMenu(self):
        self.menu = QMenu()
        self.menu1 = QMenu()
        self.showAction1 = QAction("显示消息1", self, triggered=self.showM)
        self.showAction2 = QAction("显示消息2", self, triggered=self.showM)
        self.quitAction = QAction("退出", self, triggered=self.quit)

        self.menu1.addAction(self.showAction1)
        self.menu1.addAction(self.showAction2)
        self.menu.addMenu(self.menu1, )

        self.menu.addAction(self.showAction1)
        self.menu.addAction(self.showAction2)
        self.menu.addAction(self.quitAction)
        self.menu1.setTitle("二级菜单")
        self.setContextMenu(self.menu)

    def MainEvent(self):
        self.activated.connect(self.iconClied)  # 把鼠标点击图标的信号和槽连接
        self.messageClicked.connect(self.mClied)  # 把鼠标点击弹出消息的信号和槽连接
        self.setIcon(QIcon("source/img/main.ico"))
        self.icon = self.MessageIcon()  # 设置图标

    def iconClied(self, reason):
        if reason == 2 or reason == 3:
            if self.parentwindow.isVisible():
                self.parentwindow.hide()
            else:
                self.parentwindow.show()

    def mClied(self):
        self.showMessage("提示", "你点了消息", self.icon)

    def showM(self):

        self.showMessage("测试", "我是消息", self.icon)

    def quit(self):
        if self.parentwindow.isVisible() is False:
            self.parentwindow.show()
        self.parentwindow.quit()
