import requests
#创建会话
s = requests.Session()
post_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2019721826779'
headers = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763',
}
formdata = {
    'email':	'17642181300',
    'icode' :'',
    'origURL':	'http://www.renren.com/home',
    'domain':	'renren.com',
    'key_id':	'1'
    'captcha_type'	'web_login',
    'password'	 :'3c68245254ff5562beaeee14bf46acabcf383fc36aa13102c0bb79952879712a',
    'rkey':	'17ca0e1068fc1aeb8a61f92cc34ac916',
    'f':	'http%3A%2F%2Fwww.renren.com%2F971688724%2Fnewsfeed%2Fphoto',
}
r = s.post(url=post_url,headers=headers,data=formdata)
get_url = 'http://www.renren.com/971697873/newsfeed/photo'
r = s.get(url=get_url,headers=headers)
print(r.text)