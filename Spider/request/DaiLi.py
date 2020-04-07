import requests
url = 'https://www.baidu.com/s?ie=UTF-8&wd=ip'
proxies = {
    'http' : 'http://114.215.95.188:3128'
}
headers = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763',
}
r = requests.get(url,headers=headers,proxies=proxies)
with open('daili.html','wb') as fp:
    fp.write(r.content)