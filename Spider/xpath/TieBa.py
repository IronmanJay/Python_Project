import requests
import urllib.request
import urllib.parse
import json
from lxml import etree

# 6218118230赵越
class Tieba:
    def __init__(self,ba_name,start_page,end_page):
        self.ba_name =ba_name
        self.start_page = start_page
        self.end_page = end_page
        self.part_url = "https://tieba.baidu.com"
        self.start_url = "https://tieba.baidu.com/f?"
        self.headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0; Nexus 6P Build/OPP3.170518.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Mobile Safari/537.36"}

    def parse_first_course(self,start_next_url):
        first_next_html_str = requests.get(url=start_next_url,headers=self.headers)
        return first_next_html_str.content.decode()

    def get_first_course(self,first_html_str):
        first_final_html_str = etree.HTML(first_html_str)
        first_course_list = first_final_html_str.xpath("//li[contains(@class,'tl_shadow tl_shadow_new')]")
        for first_course in first_course_list:
            first_item = {}
            first_item["标题"] = first_course.xpath("./a/div[@class='ti_title']/span/text()")[0] if len(first_course.xpath("./a/div[@class='ti_title']/span/text()")) > 0 else None
            first_href = self.part_url + first_course.xpath("./a/@href")[0] if len(first_course.xpath("./a/@href")) > 0 else None
            second_item = self.get_second_course(first_href)
            final_result = dict(first_item, **second_item)
            self.save_course(final_result)

    def get_second_course(self,first_href):
        second_response_html = requests.get(url=first_href,headers=self.headers).content.decode()
        second_final_html_str_a = etree.HTML(second_response_html)
        a = second_final_html_str_a.xpath("//*")
        for second_final_html_str in a:
            second_item = {}
            second_item["用户名"] = second_final_html_str.xpath("//div[@id='main']/div/ul/li/div/div/div/div[2]/span/a/text()")
            second_item["用户评论"] = second_final_html_str.xpath("//div[@id='main']//div[@class='content']/text()")
            second_item["图片"] = second_final_html_str.xpath("//div[@id='main']//div[@class='content']/div/div/img/@src")
        return second_item

    def save_course(self,final_result):
        file_path = self.ba_name + ".txt"
        with open(file_path,"a",encoding="utf-8") as fp:
            fp.write(json.dumps(final_result,ensure_ascii=False,indent=2))
            fp.write("\n")

    def run(self):
        for page in range(self.start_page, self.end_page + 1):
            data = {
                "kw" : self.ba_name,
                "pn" : page
            }
            data = urllib.parse.urlencode(data)
            start_next_url = self.start_url + data
            print("开始下载第%s页" % page)
            first_html_str = self.parse_first_course(start_next_url)
            self.get_first_course(first_html_str)
            print("结束下载第%s页" % page)

if __name__ == '__main__':
    ba_name = input("请输入您要爬取的吧名字:")
    start_page = int(input("请输入您要爬取的开始页码:"))
    end_page = int(input("请输入您要爬取的结束页码:"))
    tieba = Tieba(ba_name,start_page,end_page)
    tieba.run()