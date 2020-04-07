import requests
from lxml import etree

class CSDN:
    def __init__(self):
        self.url = "https://ss.csdn.net/p?http://mmbiz.qpic.cn/mmbiz_gif/KfLGF0ibu6cIIYhg3r7dibIgTKuZboVH2Y2JcC5s6qts7ic1TVQdEDwSLzS8RakA71Pc61cxWSDa9oyVrfY79eC9A/640?wx_fmt=gif&wxfrom=5&wx_lazy=1"
        self.headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36"}

    def get_href(self):
        f = open("a.txt",encoding="utf-8")
        response = f.read()
        html = etree.HTML(response)
        href = html.xpath("//div[@class='htmledit_views']/div/p/img/@src")
        p = 0
        for i in href:
            print(i)
            a = requests.get(i)
            filepath = str(p) + ".jpg"
            with open(filepath,"wb") as fp:
                fp.write(a.content)
            p = p+1

    def run(self):
        self.get_href()

if __name__ == '__main__':
    csdn = CSDN()
    csdn.run()