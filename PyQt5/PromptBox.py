import sys
from PyQt5.QtWidgets import QWidget,QToolTip,QPushButton,QApplication
from PyQt5.QtGui import QFont

# 提示信息
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.setGeometry(300,300,300,220)
    w.setWindowTitle('提示框')
    QToolTip.setFont(QFont('华文宋体',20))
    w.setToolTip('这是一个窗口\n设计者:赵越')
    button = QPushButton('Button',w)
    button.setToolTip('这是一个按钮\n设计者:赵越')
    button.resize(button.sizeHint())
    button.move(50,50)
    w.show()
    sys.exit(app.exec_())