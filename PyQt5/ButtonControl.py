import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor

# 按钮控件
class PushButton(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.color = QColor(0,0,0)
        redButton = QPushButton('红',self)
        redButton.setCheckable(True)
        redButton.move(10,10)
        redButton.clicked[bool].connect(self.setColor)

        greenButton = QPushButton('绿', self)
        greenButton.setCheckable(True)
        greenButton.move(10, 60)
        greenButton.clicked[bool].connect(self.setColor)

        blueButton = QPushButton('蓝', self)
        blueButton.setCheckable(True)
        blueButton.move(10, 110)
        blueButton.clicked[bool].connect(self.setColor)

        self.square = QFrame(self)
        self.square.setGeometry(150,20,100,100)
        self.square.setStyleSheet('QWidget{background-color:%s}'%self.color.name())
        self.setGeometry(300,300,280,170)
        self.setWindowTitle('按钮控件')
        self.show()

    def setColor(self,pressed):
        source = self.sender()
        if(pressed):
            val = 255
        else:
            val = 0
        if source.text() == '红':
            self.color.setRed(val)
        elif source.text() == '绿':
            self.color.setGreen(val)
        else:
            self.color.setBlue(val)
        self.square.setStyleSheet('QWidget{background-color:%s}' % self.color.name())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    pb = PushButton()
    sys.exit(app.exec())