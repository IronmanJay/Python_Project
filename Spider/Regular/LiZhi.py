import urllib.request
import urllib.parse
import re
def handle_request(url,page=None):
    #拼接出来指定url
    if page != None:
        url = url + str(page) + '.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763',
    }
    request = urllib.request.Request(url=url,headers=headers)
    return request
def get_text(a_href):
    #调用函数，构建请求对象
    request = handle_request(a_href)
    #发送请求，获取响应
    content = urllib.request.urlopen(request).read().decode()
    #解析内容
    pattern = re.compile(r'<div class="neirong">(.*?)</div>',re.S)
    #获取内容
    lt = pattern.findall(content)
    text = lt[0]
    #写正则，将内容里面所有的图片全部清空
    pat = re.compile(r'<img .*?>')
    text = pat.sub('',text)
    #返回内容
    return text
def parse_content(content):
    #写正则
    pattern = re.compile(r'<h3><a href="(/niandujingdianyulu/2013yulu/\d+\.html)">(.*?)</a></h3>')
    #返回的lt是一个列表，列表中的元素都是元组，元组中第一个元素就是正则中第二个小括号匹配到的内容
    lt = pattern.findall(content)
    #遍历列表
    for href_title in lt:
        #获取内容的链接
        a_href = 'http://www.yikexun.cn' + href_title[0]
        #获取标题
        title = href_title[-1]
        #向a_href发送请求,获取响应内容
        text = get_text(a_href)
        #写入到html文件中
        string = '<h1>%s</h1>%s' % (title,text)
        with open('lizhi.html','a',encoding='utf8') as fp:
            fp.write(string)
def main():
    url = 'http://www.yikexun.cn/niandujingdianyulu/2013yulu/list_60_'
    start_page = int(input("请输入起始页码："))
    end_page = int(input("请输入结束页码："))
    for page in range(start_page,end_page+1):
        #根据url和page去生成指定的request
        request = handle_request(url,page)
        #发送请求
        content = urllib.request.urlopen(request).read().decode()
        #解析内容
        parse_content(content)
if __name__ == '__main__':
    main()