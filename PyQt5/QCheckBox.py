import sys
from PyQt5.QtWidgets import *

class CheckBox(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cb = QCheckBox('请选择',self)
        cb.move(20,20)
        # cb.toggle()
        cb.stateChanged.connect(self.changeTitle)
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('还没有选择')
        self.show()

    def changeTitle(self,state):
        if state == Qt.Checked:
            self.setWindowTitle('已经选择')
        else:
            self.setWindowTitle('还没有选择')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cb = CheckBox()
    sys.exit(app.exec())