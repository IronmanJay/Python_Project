from selenium import webdriver
from lxml import etree
import urllib.request
import urllib.parse
import os
import json

# version:1.0
class ZhiLianZhaoPin:

    # 初始化参数
    def __init__(self,occupation,page):
        self.url = "https://sou.zhaopin.com/?jl=620&kt=3" # url
        # self.city = city # 城市
        self.occupation = occupation # 职业
        self.page = page # 页码

    # 可拓展功能，暂不使用
    # 使用字典键值对的方式，根据用户输入内容进行拼接url
    def get_citynum(self, city_name):
        item = {
            '上海': 538, '江苏': 538, '浙江': 540, '安徽': 541, '福建': 542, '江西': 543, '山东': 544,'河南': 545,
            '湖北': 546, '湖南': 547, '广东': 548, '广西': 549, '海南': 550, '重庆': 551,'四川': 552, }
        return item[city_name]

    # 拼接字符串并返回
    def get_url(self):
        data = {
            'kw' : self.occupation,
            'p': self.page,
        }
        final_data = urllib.parse.urlencode(data)
        url = self.url + final_data
        return url

    # 获取信息
    def get_info(self,html):
        print("=================正在保存第%d页=================" % self.page)
        info = etree.HTML(html)
        all_info = info.xpath("//div[@class='contentpile__content__wrapper clearfix']/div/a")
        item = {}
        for data in all_info:
            item["职位"] = data.xpath("./div[1]/div/span/text()")
            item["薪资"] = data.xpath("./div[2]/div/p/text()")
            item["地点"] = data.xpath("./div[2]/div/ul/li[1]/text()")
            item["经验"] = data.xpath("normalize-space(./div[2]/div/ul/li[2]/text())")
            item["学历"] = data.xpath("./div[2]/div/ul/li[3]/text()")
            item["形式"] = data.xpath("./div[2]/div[2]/span[1]/text()")
            item["规模"] = data.xpath("./div[2]/div[2]/span[2]/text()")
            item["公司"] = data.xpath("./div/div[2]/a/text()")
            item["待遇"] = data.xpath("./div[3]/div//text()")
            print(item)
            self.save_data(item)

    # 保存
    def save_data(self,item):
        if not os.path.exists(self.occupation):
            os.mkdir(self.occupation)
        filename = self.occupation + ".txt"
        filepath = self.occupation + "/" + filename
        with open(filepath,"a",encoding="utf-8") as tf:
            tf.write(json.dumps(item,ensure_ascii=False,indent=2))
            tf.write("\n")

    # 发送请求
    def get_html(self):
        url = self.get_url()
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging']) # 防止被识别
        # opt.add_argument("--proxy-server=http://117.88.176.216:3000") # 代理太慢，不推荐
        # opt.add_argument('User-Agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"') # 设置请求头
        driver = webdriver.Chrome(options=opt)
        driver.get(url)
        driver.refresh()
        html = driver.page_source
        print("=================正在获取第%d页=================" %self.page)
        self.get_info(html)
        driver.quit() # 每爬完一页就退出

    def run(self):
        self.get_html()

if __name__ == '__main__':
    # city = input("请输入您想获取的城市名称:")
    occupation = input("请输入您想获取的职业:")
    start_page = int(input("请输入开始页码:"))
    end_page = int(input("请输入结束页码:"))
    for page in range(start_page,end_page + 1):
        zhilianzhaopin = ZhiLianZhaoPin(occupation,page)
        zhilianzhaopin.run()
