import urllib.request
import urllib.parse
from pprint import pprint
import json
url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&"
headers = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763',
}
page = int(input("请输入您想爬取的页码:"))
number = 20
data = {
    "start" : (page - 1) * 20,
    "limit" : number
}
date_final = urllib.parse.urlencode(data)
url_final = url.format(date_final)
request = urllib.request.Request(url=url_final,headers=headers)
response = urllib.request.urlopen(request)
ret = json.loads(response.read().decode())
r = json.dumps(ret,ensure_ascii=False)
with open("a.html","w",encoding="utf-8") as fp:
    fp.write(r)
