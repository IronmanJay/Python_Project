# -*- coding:utf-8 -*-

from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget
from PyQt5 import uic
import configparser
import pandas as pd
import re
import json



class DataLabeling(QWidget):
    def __init__(self):
        super(DataLabeling, self).__init__()
        self.config = configparser.ConfigParser()
        self.config.read("config.cfg")

        self.ui = uic.loadUi("data_labeling_ui.ui")

        self.data_path = self.config["config"]["data_path"]
        self.current_id = int(self.config["config"]["current_id"])
        self.df = pd.read_excel(self.data_path)
        self.data = self.df.iloc[:, [2, 5]].values

        self.ui.current_id.returnPressed.connect(self.nextText)
        self.ui.previous_text.clicked.connect(self.previousText)
        self.ui.next_text.clicked.connect(self.nextText)
        self.ui.save_button.clicked.connect(self.saveButton)
        self.ui.undo_button.clicked.connect(self.undoButton)
        self.ui.copy_button.clicked.connect(self.copyButton)
        self.ui.source_text.itemDoubleClicked.connect(self.selectEvidence)
        self.ui.evidence_text.itemClicked.connect(self.deleteEvidence)

        self.ui.previous_text.setShortcut(self.config["shortcut"]["previous"])
        self.ui.next_text.setShortcut(self.config["shortcut"]["next"])
        self.ui.save_button.setShortcut(self.config["shortcut"]["save"])
        self.ui.undo_button.setShortcut(self.config["shortcut"]["undo"])
        self.ui.copy_button.setShortcut(self.config["shortcut"]["copy"])


        self.showText()

    def previousText(self):
        current_id = int(self.ui.current_id.text())
        if current_id != self.current_id:
            self.current_id = current_id
        else:
            self.current_id -= 1
        self.showText()

    def nextText(self):
        current_id = int(self.ui.current_id.text())
        if current_id != self.current_id:
            self.current_id = current_id
        else:
            self.current_id += 1
        self.showText()

    def saveButton(self):
        res = {
                "id": 0,
                "title": "",
                "content": "",
                "evidence": [],
                "ref": "",
                "sup": "",
                "nei": ""
            }
        res["id"] = self.current_id
        res["title"] = self.data[self.current_id - 1][0]
        res["content"] = self.data[self.current_id - 1][1]
        for i in range(self.ui.evidence_text.count()):
            res["evidence"].append(self.ui.evidence_text.item(i).text())
        res["ref"] = self.ui.ref_text.toPlainText()
        res["sup"] = self.ui.sup_text.toPlainText()
        res["nei"] = self.ui.nei_text.toPlainText()
        with open(self.config["config"]["output_path"], "a", encoding="utf8") as f:
            f.write(json.dumps(res) + "\n")
            # f.write(str(res) + "\n")
        QMessageBox.information(self, "保存", self.tr("保存成功！"))
        # self.nextText()
        self.showText()

    def undoButton(self):
        with open(self.config["config"]["output_path"], "r", encoding="utf8") as f:
            data = f.readlines()
        with open(self.config["config"]["output_path"], "w", encoding="utf8") as f:
            for line in data[:-1]:
                f.write(line)
        QMessageBox.information(self, "撤销", self.tr("撤销成功！"))
        self.previousText()

    def copyButton(self):
        currentItem = self.ui.source_text.currentItem()
        if currentItem is not None:
            clipboard = QApplication.clipboard()
            clipboard.setText(currentItem.text())

    def selectEvidence(self):
        self.ui.evidence_text.addItem(self.ui.source_text.currentItem().text())

    def deleteEvidence(self):
        self.ui.evidence_text.takeItem(self.ui.evidence_text.currentRow())

    def showText(self):
        if (self.current_id - 1) < 0 or self.current_id > len(self.data):
            self.current_id = 1
            QMessageBox.warning(self, "警告", self.tr("超出新闻条数范围！"), QMessageBox.Cancel)
        self.ui.source_text.clear()
        self.ui.evidence_text.clear()
        self.ui.sup_text.clear()
        self.ui.nei_text.clear()
        self.ui.ref_text.clear()
        self.ui.current_id.setText(str(self.current_id))
        self.ui.title_text.setText(self.data[self.current_id - 1][0])
        self.ui.source_text.addItems(self.cut_sent(self.data[self.current_id - 1][1]))
        self.config.set("config", "current_id", str(self.current_id))
        self.config.write(open("config.cfg", 'w', encoding="utf8"))

    def cut_sent(self, para):
        para = para.replace("”", "")
        para = para.replace("“", "")
        para = para.replace("’", "")
        para = para.replace("‘", "")
        para = para.replace(",", "，")
        # para = re.sub('(?<=[\u4e00-\u9fa5]) (?=[\u4e00-\u9fa5])', '。', para)
        para = re.sub('([。！？\?])([^”’])', r"\1\n\2", para)  # 单字符断句符
        para = re.sub('(\.{6})([^”’])', r"\1\n\2", para)  # 英文省略号
        para = re.sub('(\…{2})([^”’])', r"\1\n\2", para)  # 中文省略号
        para = re.sub('([。！？\?][”’])([^，。！？\?])', r'\1\n\2', para)
        # 如果双引号前有终止符，那么双引号才是句子的终点，把分句符\n放到双引号后，注意前面的几句都小心保留了双引号
        para = para.rstrip()  # 段尾如果有多余的\n就去掉它
        para_list = [x.strip() for x in para.split("\n") if x.strip() != ""]
        # 很多规则中会考虑分号;，但是这里我把它忽略不计，破折号、英文双引号等同样忽略，需要的再做些简单调整即可。
        return para_list


if __name__ == '__main__':
    app = QApplication([])
    stats = DataLabeling()
    stats.ui.show()
    app.exec_()