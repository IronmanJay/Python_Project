import sys
from PyQt5.QtWidgets import *

# 网格布局
class GridLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        title = QLabel('标题')
        author = QLabel('作者')
        summary = QLabel('摘要')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        summaryEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(title,1,0)
        grid.addWidget(titleEdit,1,1)
        grid.addWidget(author,2,0)
        grid.addWidget(authorEdit,2,1)
        grid.addWidget(summary,3,0)
        grid.addWidget(summaryEdit,3,1)
        self.setLayout(grid)
        self.setGeometry(300,300,350,300)
        self.setWindowTitle('网格布局')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gl = GridLayout()
    sys.exit(app.exec())