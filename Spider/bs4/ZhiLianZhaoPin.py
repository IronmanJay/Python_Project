import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import json
import time
class ZhiLianSpider(object):
    #url中不变的内容,要和参数进行拼接组成完整的url
    url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?'
    def __init__(self,jl,kw,start_page,end_page):
        #将上面的参数都保存为自己的成员属性
        self.jl = jl
        self.kw = kw
        self.start_page = start_page
        self.end_page = end_page
        #定义一个空列表，用来存放所有的工作信息
        self.items = []
    #根据page拼接指定的url，然后生成请求对象
    def handle_request(self,page):
        data = {
            'jl' : self.jl,
            'kw' : self.kw,
            'p' : page
        }
        url_now = self.url + urllib.parse.urlencode(data)
        print(url_now)
        #构建请求对象
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763',
        }
        request = urllib.request.Request(url=url_now,headers=headers)
        return request
    #解析内容函数
    def parse_content(self,content):
        #生成对象
        soup = BeautifulSoup(content,'lxml')
        #思路：先找到所有的table，因为一个工作岗位就是一个table，遍历这个table的列表，然后通过table对象的select、find方法去找每一条记录的具体信息
        table_list = soup.select('#newlist_list_content_table > table')[1:]
        #遍历table_list，依次获取每一个数据
        for table in table_list:
            #获取职位名称
            zwmc = table.select('.zwmc > div > a')[0].text
            #获取公司名称
            gsmc = table.select('.gsmc > a')[0].text
            #获取职位月薪
            zwyx = table.select('.zwyx')[0].text
            #获取工作地点
            gzdd = table.select('.gzdd')[0].text
            #获取发布时间
            gxsj = table.select('.gxsj > span')[0].text
            #存放到字典中
            item = {
                '职位名称' : zwmc,
                '公司名称' : gsmc,
                '职位月薪' : zwyx,
                '工作地点' : gzdd,
                '更新时间' : gxsj,
            }
            #再存放到列表中
            self.items.append(item)
    #爬取程序
    def run(self):
        #循环爬取每一页数据
        for page in range(self.start_page,self.end_page + 1):
            print('开始爬取第%s页' % page)
            request = self.handle_request(page)
            #发送请求，获取内容
            content = urllib.request.urlopen(request).read().decode()
            #解析内容
            self.parse_content(content)
            print('结束爬取第%s页' % page)
            time.sleep(2)
        #将列表数据保存到文件中
        # string = json.dump(self.items,ensure_ascii=False)
        with open('zhilian.txt','w',encoding='utf8') as fp:
            fp.write(str(self.items))
def main():
    jl = input("请输入工作地点：")
    kw = input("请输入工作关键字：")
    start_page = int(input("请输入起始页码："))
    end_page = int(input("请输入结束页码："))
    #创建对象，启动爬取程序
    spider = ZhiLianSpider(jl,kw,start_page,end_page)
    spider.run()
if __name__ == '__main__':
    main()