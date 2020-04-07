import requests
from lxml import etree
import urllib.request
import urllib.parse
import time

class PaiMai:

    def __init__(self,start_page,end_page):
        self.start_page = start_page
        self.end_page = end_page
        self.url = "http://artso.artron.net/auction/search_auction.php?keyword=&Status=0&ClassCode=&ArtistName=%E9%BD%90%E7%99%BD%E7%9F%B" \
                   "3&OrganCode=&StartDate=&EndDate=&listtype=0&order=&EvaluationType=&Estartvalue=&Eendvalue=&Sstartvalue=&Sendvalue=&"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36"}


    def parse(self,url):
        html = requests.get(url=url,headers=self.headers)
        return html.content.decode()

    def get_course(self,html_str):
        html = etree.HTML(html_str)
        data = html.xpath("//div[@class='relaRecom']/div/ul/li")
        for li in data:
            item = {}
            item["名称"] = li.xpath("./h3/a/text()")
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
            time.sleep(5)
            self.get_course(html_str)
            print("结束下载第%s页" % page)


if __name__ == '__main__':
    start_page = int(input("请输入您想开始的页码:"))
    end_page = int(input("请输入您想结束的页面:"))
    paimai = PaiMai(start_page,end_page)
    paimai.run()