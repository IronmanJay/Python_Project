import requests
from lxml import etree
import urllib.request
import urllib.parse
import time

class PaiMai:

    def __init__(self,start_page,end_page):
        self.start_page = start_page
        self.end_page = end_page
        self.url = "http://artso.artron.net/artist/search_artist.php?keyword=&Class=&BirthArea=&Graduated=&"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36"}

    def parse(self,url):
        html = requests.get(url=url,headers=self.headers)
        return html.content.decode()

    def get_first_course(self,html_str):
        html = etree.HTML(html_str)
        href = html.xpath("//div[@class='listPic baseTxt']/dl/dd/div/a[1]/@href") if len(html.xpath("//div[@class='listPic baseTxt']/dl/dd/div/a[1]/@href")) > 0 else None
        if href is None:
            print("此页的作者没有可拍卖的作品")
        else:
            for i in href:
                html_second = self.parse(i)
                self.get_detail_course(html_second)
                time.sleep(2)

    def get_detail_course(self,html_second):
        html = etree.HTML(html_second)
        data = html.xpath("//div[@class='relaRecom']/div/ul/li")
        for li in data:
            item = {}
            item["作者"] = html.xpath("//div[@class='result']/span/text()")
            item["作品名称"] = li.xpath("./h3/a/text()")
            item["状态"] = li.xpath("./p[1]/span/text()")
            item["LOT号"] = li.xpath("./p[2]/em/text()")
            item["估价"] = li.xpath("./p[3]/em/i[1]/text()")
            item["成交价(万元)"] = li.xpath("./p[4]/em/i[1]/text()")
            item["拍卖公司"] = li.xpath("./p[5]/em/a/text()")
            item["拍卖日期"] = li.xpath("./p[6]/em/i/text()")
            self.save(item)

    def save(self,item):
        with open('data.txt', "a", encoding="utf-8") as fp:
            fp.write(str(item))
            fp.write("\n")

    def run(self):
        for page in range(self.start_page,self.end_page+1):
            data = {"page":page}
            data = urllib.parse.urlencode(data)
            final_url = self.url + data
            print("开始下载第%s页" %page)
            html_str = self.parse(final_url)
            time.sleep(10)
            self.get_first_course(html_str)
            print("结束下载第%s页" % page)

if __name__ == '__main__':
    start_page = int(input("请输入您想开始的页码:"))
    end_page = int(input("请输入您想结束的页面:"))
    paimai = PaiMai(start_page,end_page)
    paimai.run()