import urllib.request
import urllib.parse
import re
import os
import time

def hand_request(url,page):
    url = url + str(page) + '/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763',
    }
    request = urllib.request.Request(url=url,headers=headers)
    return request

def download_image(content):
    pattern = re.compile(r'<div class="thumb">.*?<img src="(.*?)" .*?>.*?</div>', re.S)
    lt = pattern.findall(content)
    print(lt)
    #遍历列表依次下载图片
    for image_src in lt:
        #先处理image_src
        image_src = 'https:' + image_src
        #发送请求下载图片
        #创建文件夹
        dirname = 'qiutu'
        if not os.path.exists(dirname):
            os.mkdir(dirname)
        #图片的名字
        filename = image_src.split('/')[-1]
        filepath = dirname + '/' + filename
        print('%s图片正在下载......' % filename)
        urllib.request.urlretrieve(image_src,filepath)
        print('%s图片结束下载......' % filename)
        time.sleep(1)

def main():
    url = 'https://www.qiushibaike.com/pic/page/'
    start_page = int(input("请输入起始页码："))
    end_page = int(input("请输入结束页码："))
    for page in range(start_page,end_page + 1):
        print("第%s页开始下载......" % page)
        #生成请求对象
        request = hand_request(url,page)
        #发送请求对象，获取相应内容
        content = urllib.request.urlopen(request).read().decode()
        #解析内容，提取所有的图片链接，下载图片
        download_image(content)
        print("第%s页开始下载结束......" % page)
        print()
        print()
        time.sleep(2)

if __name__ == '__main__':
    main()