import sys
from PyQt5.QtWidgets import *

# QLineEdit控件
class LineEdit(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.label = QLabel(self)
        lineEdit = QLineEdit(self)
        lineEdit.move(80,100)
        self.label.move(80,40)
        lineEdit.textChanged[str].connect(self.onChanged)
        self.setGeometry(300,300,280,170)
        self.setWindowTitle('QLineEdit控件')
        self.show()

    def onChanged(self,text):
        self.label.setText(text)
        self.label.adjustSize()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    le = LineEdit()
    sys.exit(app.exec())