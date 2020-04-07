import sys
from PyQt5.QtWidgets import *

# 菜单
class memu(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('文件')
        newAction = QAction('新建',self)
        importMenu = QMenu('导入',self)
        importAction1 = QAction('从PDF导入',self)
        importAction2 = QAction('从Word导入',self)
        importAction1.triggered.connect(self.actionHandler1)
        importAction2.triggered.connect(self.actionHandler2)
        importMenu.addAction(importAction1)
        importMenu.addAction(importAction2)
        fileMenu.addAction(newAction)
        fileMenu.addMenu(importMenu)
        # menubar.setNativeMenuBar(False) 苹果系统设置菜单位置
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('菜单')
        self.show()

    def actionHandler1(self):
        print("从PDF导入")

    def actionHandler2(self):
        print("从Word导入")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    me = memu()
    sys.exit(app.exec())