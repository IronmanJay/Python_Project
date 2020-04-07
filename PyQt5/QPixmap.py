import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# QPixmao
class Pixmap(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)
        pixmap = QPixmap('Icon.jpg')
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        hbox.addWidget(lbl)
        self.setLayout(hbox)
        self.move(300,200)
        self.setWindowTitle('显示图像')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gl = Pixmap()
    sys.exit(app.exec())
