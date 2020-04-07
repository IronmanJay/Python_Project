import sys
from PyQt5.QtWidgets import *

# 盒布局:1、水平盒布局 2、垂直盒布局
class BoxLayout(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        okButton = QPushButton('确定')
        cancelButton = QPushButton('取消')
        # 创建水平盒布局
        hbox = QHBoxLayout()
        # 让两个按钮始终在窗口右侧
        hbox.addStretch()
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        # 创建垂直盒布局
        vbox = QVBoxLayout()
        vbox.addStretch()
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('盒布局')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    bl = BoxLayout()
    sys.exit(app.exec())