import urllib.request
import urllib.parse
import os
url = 'http://tieba.baidu.com/f?ie=utf-8'
ba_name = input("请输入要爬取的吧名：")
start_page = int(input("请输入要爬取的起始页码："))
end_page = int(input("请输入要爬取的结束页码："))
if not os.path.exists(ba_name):
    os.mkdir(ba_name)
for page in range(start_page,end_page + 1):
    data = {
        'kw' : ba_name,
        'pn' : (page - 1) * 50
    }
    data = urllib.parse.urlencode(data)
    url_t = url + data
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763',
    }
    request = urllib.request.Request(url=url_t,headers=headers)
    print('第%s页开始下载......' %page)
    response = urllib.request.urlopen(request)
    filename = ba_name + '_' + str(page) + '.html'
    filepath = ba_name + "/" + filename
    with open(filepath,'wb') as fp:
        fp.write(response.read())
    print('第%s页结束下载......' % page)