import sys
from PyQt5.QtWidgets import *

# 窗口居中
class CenterWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(250, 150)
        self.setWindowTitle('窗口居中')
        self.show()
        self.center()

    def center(self):
        desktop = app.desktop()
        self.move((desktop.width() - self.width())/2,(desktop.height() - self.height())/2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    cw = CenterWindow()
    sys.exit(app.exec())