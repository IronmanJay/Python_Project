import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

#QCalendarWidget
class CalendarWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout(self)
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.clicked[QDate].connect(self.showDate)
        vbox.addWidget(cal)
        date = cal.selectedDate()
        self.lbl = QLabel(self)
        self.lbl.setText(date.toString())
        vbox.addWidget(self.lbl)
        self.setLayout(vbox)
        self.setGeometry(300,300,350,300)
        self.setWindowTitle('Calendar控件')
        self.show()

    def showDate(self,date):
        self.lbl.setText(date.toString())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    qc = CalendarWidget()
    sys.exit(app.exec())