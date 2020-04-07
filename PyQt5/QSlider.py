import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

# QSlider控件
class Slider(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        slider = QSlider(Qt.Horizontal,self)
        slider.setMinimum(10)
        slider.setMaximum(500)
        slider.setGeometry(30,40,100,30)
        slider.valueChanged[int].connect(self.changeValue)
        self.label = QLabel(self)
        self.label.setGeometry(160,40,80,30)
        self.setGeometry(300,300,280,170)
        self.setWindowTitle('QSlider控件')
        self.show()

    def changeValue(self,value):
        self.label.setText(str(value))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    qs = Slider()
    sys.exit(app.exec())