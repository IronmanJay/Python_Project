import requests
from bs4 import BeautifulSoup
#创建会话
s = requests.Session()
#访问登陆页面，获取登录需要的一些参数
get_url = 'http://account.chinaunix.net/login/?url=http%3A%2F%2Fbbs.chinaunix.net%2F'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763',
}
r = s.get(get_url,headers=headers)
#生成soup对象，获取formhash值
soup = BeautifulSoup(r.text,'html')
#通过属性选择器获取对应的值
formhash = soup.select('input[name=formhash]')[0]['value']
#向指定的post发送请求
post_url = 'http://account.chinaunix.net/login/login'
formdata = {
    'formhash': formhash,
    'username':	'IronmanJay',
    'password':	'mimanibuzhidao',
    '_token':	'qqbHnApUHBiTdqz8m6CLCHQDViiajhnNR2nhS91R',
    '_t':	'1565091139850',
}
r = s.post(url=post_url,headers=headers,data=formdata)
#访问登陆后的页面
info_url = 'http://bbs.chinaunix.net/home.php?mod=space&uid=69944064&do=profile'
r = s.get(url=info_url,headers=headers)
with open('info.html','wb') as fp:
    fp.write(r.content)