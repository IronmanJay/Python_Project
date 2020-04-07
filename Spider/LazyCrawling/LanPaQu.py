import urllib.request
import urllib.parse
from lxml import etree
import time
import os
def handle_request(url,page):
    #由于第一页和后面的页码规律不一样，所以要进行判断
    if page == 1:
        url = url.format('')
    else:
        url = url.format('_' + str(page))
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763',
    }
    request = urllib.request.Request(url=url,headers=headers)
    return request
#解析内容并且下载图片
def parse_content(content):
    tree = etree.HTML(content)
    image_list = tree.xpath('//div[@id="container"]/div/div/a/img/@src2')
    #遍历列表，依次下载图片
    for image_src in image_list:
        download_image(image_src)
def download_image(image_src):
    dirpath = 'tupian'
    #创建一个文件夹
    if not os.path.exists(dirpath):
        os.mkdir(dirpath)
    #文件名
    filename = os.path.basename(image_src)
    #图片路径
    filepath = os.path.join(dirpath,filename)
    #发送请求，保存图片
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763',
    }
    request = urllib.request.Request(url=image_src,headers=headers)
    response = urllib.request.urlopen(request)
    with open(filepath,'wb') as fp:
        fp.write(response.read())
def main():
    url = 'http://sc.chinaz.com/tupian/xingganmeinvtupian{}.html'
    start_page = int(input("请输入起始页码："))
    end_page = int(input("请输入结束页码："))
    for page in range(start_page,end_page + 1):
        request = handle_request(url,page)
        content = urllib.request.urlopen(request).read().decode()
        parse_content(content)
        time.sleep(2)
if __name__ == '__main__':
    main()