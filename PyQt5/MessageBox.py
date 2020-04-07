import sys
from PyQt5.QtWidgets import QWidget,QMessageBox,QApplication

# 关闭窗口
# 封装窗口代码的类
class Message(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('对话框')
        # 显示窗口
        self.show()

    # 窗口的关闭事件
    def closeEvent(self, event):
        # 显示询问对话框
        reply = QMessageBox.question(self,'消息','您真的要退出吗?',QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accapt()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mb = Message()
    sys.exit(app.exec())