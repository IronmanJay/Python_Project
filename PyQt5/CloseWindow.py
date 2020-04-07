import sys
from PyQt5.QtWidgets import QWidget,QPushButton,QApplication
from PyQt5.QtCore import QCoreApplication

# 关闭窗口
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.setGeometry(300,300,300,220)
    w.setWindowTitle('关闭窗口')
    button = QPushButton('关闭窗口',w)
    button.clicked.connect(QCoreApplication.instance().quit)
    button.move(50,50)
    w.show()
    sys.exit(app.exec_())