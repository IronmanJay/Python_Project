import requests
from bs4 import BeautifulSoup
import time
from lxml import etree
import json
from selenium import webdriver
'''
接口信息为：
http://365yg.com/api/pc/feed/?max_behot_time=1565330116&category=video_new&utm_source=toutiao&widen=1&tadrequire=true&as=A1859DE40D019D3&cp=5D4DE1891DF39E1&_signature=7w-VrhATsk3g0iH9kTqHvO8Plb
'''
headers = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763',
}
def handle_title(widen):
    #将捕获接口拿过来
    url = 'http://365yg.com/api/pc/feed/?max_behot_time=1565330116&category=video_new&utm_source=toutiao&widen={}&tadrequire=true&as=A1859DE40D019D3&cp=5D4DE1891DF39E1&_signature=7w-VrhATsk3g0iH9kTqHvO8Plb'
    #将widen和url拼接起来，组成完整的url
    url = url.format(widen)
    #发送请求
    r = requests.get(url=url,headers=headers)
    #解析内容（返回的是json格式数据，直接解析json格式）
    #通过分析，需要data里面的 title\source_url
    #将json数据转化为python对象
    obj = json.loads(r.text)
    #取出所有和视频相关的数据,data是一个列表,里面存放的都是字典
    data = obj['data']
    #循环data列表，依次取出每一个视频信息
    for video_data in data:
        title = video_data['title']
        a_href = 'http://www.365yg.com' + video_data['source_url']
        #发送请求，获取内容，解析内容，获取src
def handle_href(a_href,title):
    #通过phantomjs来进行解决,
    browser = webdriver.PhantomJS(r'D:\Video\phantomjs-2.1.1-windows\bin\phantomjs.exe')
    browser.get(a_href)
    time.sleep(3)
    #获取源码，生成tree对象，然后查找video里面的src属性
    tree = etree.HTML(browser.page_source)
    video_src = tree.xpath('//video[@mediatype="video"]/@src')
    filepath = 'DownLoad/' + title + '.mp4'
    print('%s开始下载。。。。。。' % title)
    r = requests.get(video_src)
    with open(filepath,'wb') as fp:
        fp.write(r.content)
    print('%s结束下载。。。。。。' % title)
def main():
    #解析首页，返回所有的标题链接
    for widen in range(1,5):
        handle_title(widen)
if __name__ == '__main__':
    main()