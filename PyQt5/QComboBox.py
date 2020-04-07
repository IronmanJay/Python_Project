import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# QComboBox
class ComboBox(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel('中国',self)
        self.lbl.move(50,150)
        combo = QComboBox(self)
        combo.addItem('中国')
        combo.addItem('美国')
        combo.addItem('法国')
        combo.addItem('德国')
        combo.addItem('俄罗斯')
        combo.addItem('澳大利亚')
        combo.move(50,50)
        combo.activated[str].connect(self.onActivated)

        combo1 = QComboBox(self)
        combo1.addItem('Item1')
        combo1.addItem('Item2')
        combo1.addItem('Item3')
        combo1.addItem('Item4')
        combo1.move(200,50)
        combo1.activated[str].connect(self.onActivated)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('QComboBox')
        self.show()

    def onActivated(self,text):
        self.lbl.setText(text)
        self.lbl.adjustSize()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    qs = ComboBox()
    sys.exit(app.exec())