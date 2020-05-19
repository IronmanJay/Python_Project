import requests
import re
import os
import time
import pymysql

class SongLoad:

    def __init__(self,start,end):
        self.start = start
        self.end = end

    def mkdir(self):
        path = os.getcwd()
        path += r"\music"
        if os.path.exists(path):
            pass
        else:
            os.mkdir(path)
        return path

    def saveMysql(self,title,sid,url):
        t = [sid,title,url]
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='990929', database='htqyy6218118230', charset='utf8')
        cur = conn.cursor()
        sql = u"INSERT INTO song(sid,title,url) VALUES(%s,%s,%s)"
        cur.execute(sql,t)
        conn.commit()
        cur.close()
        conn.close()

    def request(self):
        for i in range(self.start,self.end + 1):
            url = r"http://www.htqyy.com/top/musicList/hot?pageIndex={}&pageSize=20".format(str(i - 1))
            response = requests.get(url).text
        return response

    def parseSongAndSave(self,titleLst,sidLst):
        for sid,name in zip(sidLst,titleLst):
            songUrl="http://f2.htqyy.com/play7/{}/mp3/4".format(str(sid))
            self.saveMysql(name,sid,songUrl)
            path = self.mkdir()
            response = requests.get(songUrl).content
            with open("{}\{}.mp3".format(path,name),"wb") as fw:
                print("{}.map3正在下载......".format(name))
                time.sleep(2)
                fw.write(response)

    def parseHtml(self,html):
        titleLst = []
        sidLst = []
        pattern1 = r'title="(.*?)" sid'
        pattern2 = r'sid="(.*?)">'
        titleLst.extend(re.findall(pattern1, html))
        sidLst.extend(re.findall(pattern2, html))
        return titleLst,sidLst

    def run(self):
        html = self.request()
        titleLst,sidLst = self.parseHtml(html)
        self.parseSongAndSave(titleLst,sidLst)

if __name__ == '__main__':
    songload = SongLoad(1,2)
    songload.run()