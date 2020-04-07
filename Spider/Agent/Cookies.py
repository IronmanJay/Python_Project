import urllib.request
import urllib.parse
import http.cookiejar
#真实的模拟浏览器，当发送完post请求的时候，将cookie保存到代码中
#创建一个cookiejar对象
cj = http.cookiejar.CookieJar()
#通过cookiejar对象创建一个handler
handler = urllib.request.HTTPCookieProcessor(cj)
#根据handler创建一个opener
opener = urllib.request.build_opener(handler)
post_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=201962147607'
formdata = {
    'email':	'17642181300',
    'icode': '',
    'origURL':'http://www.renren.com/home',
    'domain':'renren.com',
    'key_id':	'1',
    'captcha_type':	'web_login',
    'password'	 :'3514e036d1f501b1da55def5b0c10f22493eef2972d37528ad13f7777e1874ec',
    'rkey':	'0e927ccd0b3208297fdef16ac05fe58d',
    'f':	'http%3A%2F%2Fwww.renren.com%2F971697873%2Fnewsfeed%2Fphoto',
}
headers = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763',
}
request = urllib.request.Request(url=post_url,headers=headers)
formdata = urllib.parse.urlencode(formdata).encode()
response = opener.open(request,data=formdata)
print(response.read().decode())
print('*' * 50)
get_url = 'http://www.renren.com/971697873/newsfeed/photo'
request = urllib.request.Request(url = get_url,headers=headers)
response = opener.open(request)
print(response.read().decode())