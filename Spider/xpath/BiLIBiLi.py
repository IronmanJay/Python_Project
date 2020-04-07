import requests
from lxml import etree
import re
import json

class BiLiBiLi:
    # 初始化方法
    def __init__(self,av_num):
        # 接收av号
        self.name = "av号" + str(av_num)
        # 拼接视频地址
        self.av_url = "https://www.bilibili.com/video/av{}".format(av_num)
        # 请求头
        self.headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}

    # 响应html内容，并返回
    def parse_url(self,av_url):
        response = requests.get(url=av_url,headers=self.headers)
        return response.content.decode()

    # 解析html内容
    def get_course(self,html_str):
        # 使用xpath
        html = etree.HTML(html_str)
        # 使用字典保存标题和oid
        item = {}
        # 这里使用xpath提取标题
        item["标题:"] = html.xpath("//div[@id='app']/div/div/div/h1/span/text()")[0] if len(html.xpath("//div[@id='app']/div/div/div/h1/span/text()")) > 0 else None
        if item["标题:"]:
            # 这里使用正则提取oid
            item["cid:"] = re.findall(r"\"pages\"\:\[\{\"cid\":(.*?)\,", html_str, re.S)[0]
        else:
            print("请输入正确的av号")
        # 返回提取到的内容
        return item

    # 解析弹幕url地址
    def get_danmu(self,item):
        oid = item["cid:"]
        # 拼接从html中获取到的oid
        danmu_url = "https://api.bilibili.com/x/v1/dm/list.so?oid={}".format(oid)
        # 发送请求
        response = requests.get(url=danmu_url,headers=self.headers)
        # 解析内容
        danmu_json = response.content.decode()
        danmu = etree.HTML(danmu_json.encode("utf-8"))
        # 使用xpath在xml中获取弹幕
        item["弹幕:"] = danmu.xpath("//d/text()")
        # 返回获取到的弹幕
        return item

    # 保存数据
    def save(self,all):
        # 保存为JSON格式到本地
        with open("{}.json".format(self.name),"a",encoding="utf8") as fp:
            fp.write(json.dumps(all,ensure_ascii=False,indent=4))

    def run(self):
        # 获取相应内容
        html_str = self.parse_url(self.av_url)
        # 提取所需数据
        item = self.get_course(html_str)
        all = self.get_danmu(item)
        # 保存数据为JSON格式到本地
        self.save(all)

# 主方法
if __name__ == '__main__':
    # 输入av号，便于之后拼接
    av_num = input("请输入av号:")
    # 传递参数
    bilibili = BiLiBiLi(av_num)
    # 调用方法
    bilibili.run()