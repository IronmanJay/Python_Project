from PyQt5.QtWidgets import QApplication,QWidget
import sys
from PyQt5.QtGui import QIcon

# 窗口图标
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.setGeometry(300,300,300,220)
    w.setWindowTitle("窗口图标")
    app.setWindowIcon(QIcon('Icon.jpg'))
    w.show()
    sys.exit(app.exec_())