import requests
'''
url = 'http://www.baidu.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763',
}
r = requests.get(url,headers=headers)
r.encoding = 'utf8'
print(r.text)
'''
#带参数的get
url = 'https://www.baidu.com/s'
data = {
    'ie' : 'utf8',
    'kw' : '中国'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763',
}
#定制头部
r = requests.get(url,headers=headers,params=data)
#查看状态码
print(r.status_code)
#查看响应头部
print(r.headers)
#查看所请求的url
print(r.url)
#把结果写入文件中
with open('baidu.html','wb') as fp:
    fp.write(r.content)