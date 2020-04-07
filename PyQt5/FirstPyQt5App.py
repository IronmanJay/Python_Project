from PyQt5.QtWidgets import QApplication,QWidget
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 创建一个窗口
    w = QWidget()
    # 设置窗口的宽度和高度
    w.resize(250,150)
    # 移动窗口位置
    w.move(300,300)
    # 设置窗口标题
    w.setWindowTitle("第一个PyQt5应用")
    w.show()
    sys.exit(app.exec_())