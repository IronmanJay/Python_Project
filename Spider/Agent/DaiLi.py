import urllib.request
import urllib.parse
#创建handler
handler = urllib.request.ProxyHandler({'http':'114.215.95.188:3128'})
#创建opener
opener = urllib.request.build_opener(handler)
url = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=ip&rsv_pq=f5e2165600567401&rsv_t=1a64zuPVi%2Fo2%2BjSGkqo9I0pXUHDZ9jnT7j3RDplNLDvG2%2BO9HWuk2CcQq70&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=3&rsv_sug1=3&rsv_sug7=101&rsv_sug2=0&inputT=478&rsv_sug4=1172'
headers = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763',
}
request = urllib.request.Request(url,headers=headers)
response = opener.open(request)
with open('ip.html','wb') as fp:
    fp.write(response.read())