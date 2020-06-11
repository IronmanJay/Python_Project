import requests
from lxml import etree
import pymysql
import re

# 初始信息
head_url = "https://www.cncn.com/top/"
headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0; Nexus 6P Build/OPP3.170518.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Mobile Safari/537.36"}

def spiderMountain6011112101():
    """爬取信息"""
    # 得到首页html
    head_html = requests.get(url=head_url,headers=headers).text
    # 使用xpath提取更多url
    head_html_str = etree.HTML(head_html)
    more_url = head_html_str.xpath("//div[@class='tit']//span/a/@href")[0]
    # 来到更多的主界面
    more_html = requests.get(url=more_url,headers=headers).content.decode('gbk','ignore')
    # 解析更多主界面
    more_html_str = etree.HTML(more_html)
    # 得到信息
    # 因为简介和名字、href不在一个标签里，所以分两次提取，首先提取名字、href
    first_info=[]
    names = more_html_str.xpath("//div[@class='resizeimg4']/div//li//a/@href")
    hrefs = more_html_str.xpath("//div[@class='resizeimg4']/div//li//a//@title")
    for mname,mhref in zip(names,hrefs):
        first_info.append((mname,mhref))
    # 然后提取简介
    second_info=[]
    introduces= more_html_str.xpath("//div[@class='resizeimg4']/p//text()")
    for introduce in introduces:
        second_info.append(introduce)
    # 将数据合并为三元组
    final_info=[]
    for first,second in zip(first_info,second_info):
        final_info.append((first[1],first[0],re.sub("[\s\n\t]", "", second)))
    # 返回数据
    return final_info

def saveDB6011112101(mInfo):
    """保存信息"""
    try:
        conn = pymysql.connect(host='localhost',port=3306,user='root',password='990929',db='db6218118230')
        cursor = conn.cursor()
        insert_sql = "insert into mountain6218118230(mname,href,introduce) values (%s,%s,%s)"
        for data in mInfo:
            cursor.execute(insert_sql,(data))
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(e)

def listAll6011112101():
    """打印信息"""
    try:
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='990929', db='db6218118230')
        cursor = conn.cursor()
        sql = "select mno,mname from mountain6218118230"
        cursor.execute(sql)
        result = cursor.fetchall()
        for items in result:
            for item in range(len(items)):
                print(items[item])
            print("\n")
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(e)

def search6011112101(id):
    """查找信息"""
    try:
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='990929', db='db6218118230')
        cursor = conn.cursor()
        sql = "select mname,href,introduce from mountain6218118230 WHERE mno=%s" % id
        cursor.execute(sql)
        result = cursor.fetchall()
        name = result[0][0]
        url = result[0][1]
        introduce = result[0][2]
        html = requests.get(url=url,headers=headers)
        html_str = etree.HTML(html.text)
        location = html_str.xpath("//div[@class='con']/text()")[0]
        time = html_str.xpath("//div[@class='con']/text()")[4]
        print("景点名字：", name)
        print("景点开放时间：", time)
        print("景点地址：", location)
        print("景点简介：", introduce)
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(e)

if __name__ == '__main__':
    # 爬取信息
    mInfo = spiderMountain6011112101()
    # 保存信息
    saveDB6011112101(mInfo)
    # 打印信息
    listAll6011112101()
    # 根据编号查找山
    id = input("请输入山的编号:")
    search6011112101(id)

