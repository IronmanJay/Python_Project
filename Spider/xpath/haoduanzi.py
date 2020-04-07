import urllib.request
import urllib.parse
from lxml import etree
import time
import json
item_list = []
def handle_request(url,page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763',
    }
    url = url % page
    print(url)
    request = urllib.request.Request(url = url, headers = headers)
    return request
def parse_content(content):
    #生成对象
    tree = etree.HTML(content)
    #抓取内容
    div_list = tree.xpath('//div[@class="log cate4 auth1"]')
    #遍历div列表
    for odiv in div_list:
        #获取标题
        title = odiv.xpath('.//h3/a/text()')[0]
        #获取内容
        text_lt = odiv.xpath('.//div[@class="cont"]/p/text()')
        text = '\n'.join(text_lt)
        item = {
            '标题' : title,
            '内容' : text,
        }
        #将内容添加到列表中
        item_list.append(item)
def main():
    start_page = int(input("请输入起始页码："))
    end_page = int(input("请输入结束页码："))
    url = 'http://www.haoduanzi.com/category-10_%s.html'
    for page in range(start_page,end_page + 1):
        request = handle_request(url,page)
        content = urllib.request.urlopen(request).read().decode()
        #解析内容
        parse_content(content)
        time.sleep(2)
    #写入到文件中
    string = json.dump(item_list,ensure_ascii=False)
    with open('duanzi.txt','w',encoding='utf8') as fp:
        fp.write(string)
if __name__ == '__main__':
    main()