import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# QProgressBar控件
class ProgressBar(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(40,40,200,25)
        self.btn = QPushButton('开始',self)
        self.btn.move(40,80)
        self.btn.clicked.connect(self.doAction)
        self.timer = QBasicTimer()
        self.value = 0
        self.setGeometry(300,300,280,170)
        self.setWindowTitle('QProgressBar控件')

    def timerEvent(self, e):
        if self.value >= 100:
            self.timer.stop()
            self.btn.setText('完成')
            return
        self.value = self.value + 1
        self.pbar.setValue(self.value)

    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('开始')
        else:
            self.timer.start(100,self)
            self.btn.setText('停止')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    qp = ProgressBar()
    sys.exit(app.exec())
