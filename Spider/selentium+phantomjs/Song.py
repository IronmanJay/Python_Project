import urllib.request
import urllib.parse
from lxml import etree
from selenium import webdriver
import re
import requests
import os
import json

class WangYiYunYinYue:
    # 初始化方法
    def __init__(self):
        # 歌手页url，待拼接
        self.info_url = "https://music.163.com/#"
        # 具体歌手内部页url，待拼接
        self.start_url = "https://music.163.com/#/discover/artist/cat?"
        # 具体歌曲url，待拼接
        self.prot_url = "https://music.163.com/#/artist?"
        # 请求头
        self.headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36"}

    def dafenlei(self,dafenlei_name):
        # 使用字典键值对的方式，根据用户输入内容进行拼接url
        item = {
            '华语男歌手' : 1001, '华语女歌手' : 1002, '华语组合/乐队' : 1003, '欧美男歌手' : 2001, '欧美女歌手' : 2002, '欧美组合/乐队' : 2003, '日本男歌手' : 6001, '日本女歌手' : 6002,
            '日本组合/乐队' : 6003, '韩国男歌手' : 7001, '韩国女歌手' : 7002, '韩国组合/乐队' : 7003, '其他男歌手' : 4001, '其他女歌手' : 4002, '其他组合/乐队' : 4003,}
        return item[dafenlei_name]

    def geshoufenlei(self,geshou):
        # 使用字典键值对的方式，根据用户输入内容进行拼接url
        item = {
            '热门' : -1, 'A' : 65, 'B' : 66, 'C' : 67, 'D' : 68, 'E' : 69, 'F' : 70, 'G' : 71, 'H' : 72, 'I' : 73, 'J' : 74, 'K' : 75, 'L' : 76, 'M' : 77, 'N' : 78,
            'O': 79,'P' : 80, 'Q' : 81, 'R' : 82, 'S' : 83, 'T' : 84, 'U' : 85, 'V' : 86, 'W' : 87, 'X' : 88, 'Y' : 89, 'Z' : 90, '其他' : 0, }
        return item[geshou]

    # 根据上面的用户输入内容，拼接url
    def get_url(self,fenlei_id,geshou_initial):
        data = {
            "id" : fenlei_id,
            "initial" : geshou_initial
        }
        # 解码
        data_final = urllib.parse.urlencode(data)
        return self.start_url + data_final

    def get_gesou_info(self,html):
        # 使用xpath获取内容
        geshou_html = etree.HTML(html)
        geshou = geshou_html.xpath("//ul[@class='m-cvrlst m-cvrlst-5 f-cb']/li")
        for list in geshou:
            item= {}
            item["歌手名称:"] = list.xpath("./a/text()") + list.xpath("./div/a/text()") + list.xpath("./p/a/text()")
            href = list.xpath("./a[1]/@href") + list.xpath("./div/a/@href")
            # 获取二级页面url
            self.get_erji_info(href)

    # 整个项目的请求方法，可以获得响应内容
    def parse_url(self,url):
        response = requests.get(url=url,headers=self.headers)
        return response.content.decode()

    # 根据get_gesou_info中获取到的二级页面url，使用正则表达式提取待拼接的内容，继续发送请求
    # 这里使用selenium控制浏览器
    def get_erji_info(self,href):
        src = href[0]
        id = re.findall(r"\d*\d",src,re.S)[0]
        data = {
            "id" : id,
        }
        finaldata = urllib.parse.urlencode(data)
        url = self.prot_url + finaldata
        driver = webdriver.Chrome()
        driver.get(url)
        driver.switch_to.frame(driver.find_element_by_name("contentFrame"))
        html = driver.page_source
        info_html = etree.HTML(html)
        next_href_list = info_html.xpath("//table[@class='m-table m-table-1 m-table-4']/tbody")
        # 获取到三级页面的url
        for next_href in next_href_list:
            next_url = next_href.xpath("./tr/td[2]/div/div/div/span/a/@href")
            self.make_sanji_url(next_url)

    # 解析三级页面的响应
    def make_sanji_url(self,next_url):
        for src in next_url:
            url = self.info_url + src
            self.get_sanji_info(url)

    # 继续获取内容，这才是核心，提取到歌词
    def get_sanji_info(self,url):
        driver_html = webdriver.Chrome()
        driver_html.get(url)
        driver_html.switch_to.frame(driver_html.find_element_by_name("contentFrame"))
        html = driver_html.page_source
        info_html = etree.HTML(html)
        all = {}
        all["歌曲名称:"] = info_html.xpath("//div[@class='cnt']/div[@class='hd']/div//text()")
        all["歌手:"] = info_html.xpath("//div[@class='cnt']/p/span/a/text()")
        all["所属专辑:"] = info_html.xpath("//div[@class='cnt']/p/a/text()")
        all["歌词:"] = info_html.xpath("//div[@class='cnt']/div[@id='lyric-content']//text()")
        self.save(all)

    # 保存方法
    def save(self,all):
        name = all["歌手:"][0]
        if not os.path.exists(name):
            os.mkdir(name)
        filename = name + ".txt"
        filepath = name + "/" + filename
        with open(filepath,"a",encoding="utf-8") as tf:
            tf.write(json.dumps(all,ensure_ascii=False,indent=2))
            tf.write("\n")

    # 主方法
    def run(self):
        dafenlei_name = input("请输入歌手分类:")
        fenlei_id = self.dafenlei(dafenlei_name)
        geshou = input("请输入歌手首字母/热门/其他:")
        geshou_initial = self.geshoufenlei(geshou)
        url = self.get_url(fenlei_id,geshou_initial)
        driver = webdriver.Chrome()
        driver.get(url)
        driver.switch_to.frame(driver.find_element_by_name("contentFrame"))
        html = driver.page_source
        self.get_gesou_info(html)
        driver.quit()

if __name__ == '__main__':
    wangyiyunyinyue = WangYiYunYinYue()
    # 调用方法
    wangyiyunyinyue.run()