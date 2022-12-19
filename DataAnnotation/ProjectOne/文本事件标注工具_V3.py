import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import csv
import pandas as pd
import pickle

RELATION_DICT = {
                    1: '无关系',
                    2: '因果关系',
                    3: '条件关系',
                    4: '反转关系',
                    5: '顺承关系',
                    6: '递进关系',
                 }
CURRENT_STATUS_PATH = './current_status.pkl'


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        # 是否完成指定内容的标注
        self.isDone = False
        # 语料的总数量
        self.total = 0
        # 当前标注的下标
        self.cur = -1
        # 从哪里开始
        self._from = -1
        # 到哪里结束
        self._to = -1
        # 语料的所有数据
        self.data = None
        self.stack = Stack()
        self.save_path = ''
        self.corpus_path = ''

        # 窗口标题
        self.setWindowTitle('事件关系标注')
        # self.resize(1120, 750)
        self.setFixedSize(1120, 750)
        self.font = QtGui.QFont()
        self.font.setFamily("黑体")
        self.font.setPointSize(10)
        self.setFont(self.font)

        textBrowser_font = QtGui.QFont()
        textBrowser_font.setFamily("黑体")
        textBrowser_font.setPointSize(15)
        self.textBrowser = QtWidgets.QTextEdit(self)
        self.textBrowser.setGeometry(QtCore.QRect(50, 50, 861, 321))
        self.textBrowser.setTextBackgroundColor(QtGui.QColor(125, 190, 159))
        self.textBrowser.setFont(textBrowser_font)

        self.content_label_1 = QtWidgets.QLabel(self)
        self.content_label_1.setGeometry(QtCore.QRect(50, 15, 71, 21))
        self.content_label_1.setText("文本1")

        self.content_edit_1 = QtWidgets.QLineEdit(self)
        self.content_edit_1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.content_edit_1.setGeometry(QtCore.QRect(100, 10, 200, 35))

        self.textBrowser_2 = QtWidgets.QTextEdit(self)
        self.textBrowser_2.setGeometry(QtCore.QRect(50, 420, 861, 321))
        self.textBrowser_2.setTextBackgroundColor(QtGui.QColor(125, 190, 159))
        self.textBrowser_2.setFont(textBrowser_font)

        self.content_label_2 = QtWidgets.QLabel(self)
        self.content_label_2.setGeometry(QtCore.QRect(50, 385, 71, 21))
        self.content_label_2.setText("文本2")

        self.content_edit_2 = QtWidgets.QLineEdit(self)
        self.content_edit_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.content_edit_2.setGeometry(QtCore.QRect(100, 380, 200, 35))

        # 关系单选按钮
        self.relation_label = QtWidgets.QLabel(self)
        self.relation_label.setGeometry(QtCore.QRect(945, 50, 141, 42))
        self.relation_label.setText("事件关系:\n(按小数字键选择)")
        self.relation_rb1 = QtWidgets.QRadioButton('无关系：  1', self)
        self.relation_rb1.setGeometry(QtCore.QRect(945, 90, 141, 31))
        self.relation_rb1.setChecked(True)
        self.relation_rb2 = QtWidgets.QRadioButton('因果关系：2', self)
        self.relation_rb2.setGeometry(QtCore.QRect(945, 120, 141, 31))
        self.relation_rb3 = QtWidgets.QRadioButton('条件关系：3', self)
        self.relation_rb3.setGeometry(QtCore.QRect(945, 150, 141, 31))
        self.relation_rb4 = QtWidgets.QRadioButton('反转关系：4', self)
        self.relation_rb4.setGeometry(QtCore.QRect(945, 180, 141, 31))
        self.relation_rb5 = QtWidgets.QRadioButton('顺承关系：5', self)
        self.relation_rb5.setGeometry(QtCore.QRect(945, 210, 141, 31))
        self.relation_rb6 = QtWidgets.QRadioButton('递进关系：6', self)
        self.relation_rb6.setGeometry(QtCore.QRect(945, 240, 141, 31))

        self.relation_rb_group = QtWidgets.QButtonGroup(self)
        self.relation_rb_group.addButton(self.relation_rb1, 1)
        self.relation_rb_group.addButton(self.relation_rb2, 2)
        self.relation_rb_group.addButton(self.relation_rb3, 3)
        self.relation_rb_group.addButton(self.relation_rb4, 4)
        self.relation_rb_group.addButton(self.relation_rb5, 5)
        self.relation_rb_group.addButton(self.relation_rb6, 6)

        self.corpus_path_edit = QtWidgets.QLineEdit(self)
        self.corpus_path_edit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.corpus_path_edit.setGeometry(QtCore.QRect(945, 320, 141, 31))

        self.corpus_path_button = QtWidgets.QPushButton(self)
        self.corpus_path_button.setGeometry(QtCore.QRect(950, 360, 131, 30))
        self.corpus_path_button.setText("设置语料路径")
        self.corpus_path_button.clicked.connect(self.get_corpus_path)

        self.save_path_edit = QtWidgets.QLineEdit(self)
        self.save_path_edit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.save_path_edit.setGeometry(QtCore.QRect(945, 410, 141, 31))

        self.save_path_button = QtWidgets.QPushButton(self)
        self.save_path_button.setGeometry(QtCore.QRect(945, 450, 131, 30))
        self.save_path_button.setText("设置保存路径")
        self.save_path_button.clicked.connect(self.get_save_path)

        self.confirm_button = QtWidgets.QPushButton(self)
        self.confirm_button.setGeometry(QtCore.QRect(955, 510, 111, 41))
        self.confirm_button.setText("确定")
        self.confirm_button.clicked.connect(self.save_relation)

        self.current_schedule = QtWidgets.QLabel(self)
        self.current_schedule.setGeometry(QtCore.QRect(920, 700, 180, 41))

        self.cur_label = QtWidgets.QLabel(self)
        self.cur_label.setGeometry(QtCore.QRect(350, 15, 150, 21))

        self.total_label = QtWidgets.QLabel(self)
        self.total_label.setGeometry(QtCore.QRect(500, 15, 150, 21))

        self.actual_label = QtWidgets.QLabel(self)
        self.actual_label.setGeometry(QtCore.QRect(660, 15, 200, 21))

        self.reset_actual_range = QtWidgets.QPushButton(self)
        self.reset_actual_range.setGeometry(QtCore.QRect(860, 10, 60, 30))
        self.reset_actual_range.setText("重置")
        self.reset_actual_range.clicked.connect(self.show_dialog)
        self.reset_actual_range.setVisible(False)

        self.load_current_status()

    def load_current_status(self):
        if os.path.exists(CURRENT_STATUS_PATH):
            with open(CURRENT_STATUS_PATH, 'rb') as f:
                current_status = pickle.load(f)

                self.corpus_path = current_status['corpus_path']
                self.save_path = current_status['save_path']
                self.total = current_status['total']
                self.cur = current_status['cur']
                self.data = current_status['data']
                self._from = current_status['from']
                self._to = current_status['to']
                self.set_textBrowser_content()
                self.save_path_edit.setText(self.save_path)
                self.corpus_path_edit.setText(self.corpus_path)
                self.cur_label.setText("当前位置：{}".format(self.cur))
                self.total_label.setText("总范围：0~{}".format(self.total))
                self.actual_label.setText("标注范围：{}~{}".format(self._from, self._to))
                self.reset_actual_range.setVisible(True)
                self.current_schedule.setText(
                    "当前标注进度：{:.2f}%".format(100 * (self.cur - self._from) / (self._to - self._from + 1)))

    def dump_current_status(self):
        current_status = {'from': self._from,
                          'to': self._to,
                          'data': self.data,
                          'save_path': self.save_path,
                          'corpus_path': self.corpus_path,
                          'total': self.total,
                          'cur': self.cur}
        with open(CURRENT_STATUS_PATH, 'wb') as f:
            pickle.dump(current_status, f)

    def set_textBrowser_content(self):

        filename1 = self.data["file_name_1"][self.cur]
        content1 = self.data["content_1"][self.cur]
        self.content_edit_1.setText(filename1)
        self.textBrowser.setText(content1)

        filename2 = self.data["file_name_2"][self.cur]
        content2 = self.data["content_2"][self.cur]
        self.content_edit_2.setText(filename2)
        self.textBrowser_2.setText(content2)

    def init_file(self):
        self.total = 0
        self.cur = 0
        self.isDone = False
        self._from = -1
        self._to = -1

    def init_windows(self):
        self.content_edit_1.setText('')
        self.textBrowser.setText('')
        self.content_edit_2.setText('')
        self.textBrowser_2.setText('')
        self.corpus_path_edit.setText('')
        self.cur_label.setText('')
        self.total_label.setText('')
        self.actual_label.setText('')
        self.relation_rb1.setChecked(True)

    def mouseReleaseEvent(self, event):
        self.textBrowser.clearFocus()
        self.textBrowser_2.clearFocus()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_1:
            self.relation_rb1.setChecked(True)
        if event.key() == QtCore.Qt.Key_2:
            self.relation_rb2.setChecked(True)
        if event.key() == QtCore.Qt.Key_3:
            self.relation_rb3.setChecked(True)
        if event.key() == QtCore.Qt.Key_4:
            self.relation_rb4.setChecked(True)
        if event.key() == QtCore.Qt.Key_5:
            self.relation_rb5.setChecked(True)
        if event.key() == QtCore.Qt.Key_6:
            self.relation_rb6.setChecked(True)
        if event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:
            self.save_relation()
        # 撤销组合键ctrl + z
        if event.key() == QtCore.Qt.Key_Z:
            if QApplication.keyboardModifiers() == QtCore.Qt.ControlModifier:
                if not self.stack.isEmpty():
                    top_item = self.stack.pop()
                    self.cur = top_item
                    if self.isDone:
                        self.isDone = not self.isDone
                        self.corpus_path_edit.setText(self.corpus_path)

                    self.cur_label.setText("当前位置：{}".format(self.cur))
                    self.actual_label.setText("标注范围：{}~{}".format(self._from, self._to))
                    self.total_label.setText("总范围：0~{}".format(self.total))
                    self.current_schedule.setText(
                        "当前标注进度：{:.2f}%".format(100 * (self.cur - self._from) / (self._to - self._from + 1)))
                    self.dump_current_status()
                    self.set_textBrowser_content()
                    data = pd.read_csv(self.save_path)
                    data = data.drop(data.tail(1).index)
                    data.to_csv(self.save_path, index=0, encoding="utf-8-sig")

    def get_save_path(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(None, "设置保存路径", "C:/")
        self.save_path_edit.setText(path)
        if path != '':
            self.save_path = os.path.join(path, 'relation.csv')

    def show_dialog(self):
        # 创建QDialog对象
        dialog = QtWidgets.QDialog()
        dialog.setFixedSize(300, 200)
        dialog.setWindowTitle("设置标注起始位置")
        dialog.setFont(self.font)
        dialog.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        total_label = QtWidgets.QLabel(dialog)
        total_label.setGeometry(QtCore.QRect(90, 30, 150, 30))
        total_label.setText("范围：{}~{}".format(0, self.total))

        from_edit = QtWidgets.QLineEdit(dialog)
        from_edit.setGeometry(QtCore.QRect(50, 80, 80, 30))
        separator_label = QtWidgets.QLabel(dialog)
        separator_label.setGeometry(QtCore.QRect(150, 80, 80, 30))
        separator_label.setText("~")
        to_edit = QtWidgets.QLineEdit(dialog)
        to_edit.setGeometry(QtCore.QRect(180, 80, 80, 30))
        # 创建按钮到新创建的dialog对象中
        btn = QtWidgets.QPushButton('确认', dialog)
        btn.setGeometry(QtCore.QRect(100, 150, 100, 30))
        btn.clicked.connect(lambda: self.close_dialog(dialog, from_edit, to_edit))
        # 设置窗口的属性为ApplicationModal模态，用户只有关闭弹窗后，才能关闭主界面
        dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        dialog.exec_()

    def close_dialog(self, component, from_edit, to_edit):
        _from = from_edit.text()
        _to = to_edit.text()
        if _from == "" or _to == "" or int(_from) < 0 or int(_to) > self.total or int(_from) > int(_to):
            QtWidgets.QMessageBox.critical(self, "error", "请输入正确的范围！", QtWidgets.QMessageBox.Ok)
            return
        self._from = int(from_edit.text())
        self._to = int(to_edit.text())
        self.cur = self._from
        self.cur_label.setText("当前位置：{}".format(self.cur))
        self.actual_label.setText("标注范围：{}~{}".format(self._from, self._to))
        self.current_schedule.setText(
            "当前标注进度：{:.2f}%".format(100 * (self.cur - self._from) / (self._to - self._from + 1)))
        self.reset_actual_range.setVisible(True)
        self.set_textBrowser_content()
        self.dump_current_status()
        component.close()

    def get_corpus_path(self):
        self.init_file()
        path = QtWidgets.QFileDialog.getOpenFileName(None, "设置语料", "./",  "Text Files (*.csv)")[0]
        if path is None or path == '':
            return
        self.data = pd.read_csv(path)
        if {'file_name_1', 'file_name_2', 'content_1', 'content_2'} != set(self.data.columns):
            self.data = None
            QtWidgets.QMessageBox.critical(self, "error", "请选择正确的语料！", QtWidgets.QMessageBox.Ok)
            return
        self.total = len(self.data) - 1
        self.actual_label.setText("标注范围：{}~{}".format(self._from, self._to))
        self.reset_actual_range.setVisible(True)
        self.show_dialog()

        self.total_label.setText("总范围：0~{}".format(self.total))

        self.corpus_path = path
        self.corpus_path_edit.setText(path)

    def save_relation(self):
        if self.save_path_edit.text() == '':
            QtWidgets.QMessageBox.warning(self, "warning", "请选择保存路径", QtWidgets.QMessageBox.Ok)
            return None
        if self.corpus_path_edit.text() == '' and self.len == 0:
            QtWidgets.QMessageBox.warning(self, "warning", "请选择语料路径", QtWidgets.QMessageBox.Ok)
            return None
        try:
            if os.path.exists(self.save_path):
                with open(self.save_path, 'a+', encoding='utf-8-sig', newline='') as f:
                    csv_writer = csv.writer(f)
                    csv_writer.writerow([self.textBrowser.toPlainText(),
                                         self.textBrowser_2.toPlainText(),
                                         RELATION_DICT[self.relation_rb_group.checkedId()]])
            else:
                with open(self.save_path, 'w', encoding='utf-8-sig', newline='') as f:
                    csv_writer = csv.writer(f)
                    csv_writer.writerow(["content1", "content2", "relation"])
                    csv_writer.writerow([self.textBrowser.toPlainText(),
                                         self.textBrowser_2.toPlainText(),
                                         RELATION_DICT[self.relation_rb_group.checkedId()]])
            QtWidgets.QMessageBox.about(self, "success", "保存成功！")
            self.stack.push(self.cur)
            self.cur += 1
            self.cur_label.setText("当前位置：{}".format(self.cur))
            self.current_schedule.setText(
                "当前标注进度：{:.2f}%".format(100 * (self.cur - self._from) / (self._to - self._from + 1)))
            if self.cur > self._to:
                self.isDone = True
            if self.isDone:
                QtWidgets.QMessageBox.about(self, "success", "该文件夹已标注完成！")
                self.init_windows()
                os.remove(CURRENT_STATUS_PATH)
            else:
                self.dump_current_status()
                self.set_textBrowser_content()
        except:
            QtWidgets.QMessageBox.critical(self, "error", "文件异常！", QtWidgets.QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = Ui_MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
