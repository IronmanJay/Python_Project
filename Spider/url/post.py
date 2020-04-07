import urllib.parse
import urllib.request
post_url = 'https://fanyi.baidu.com/sug'
word = input("请输入您要查找的英文单词:")
form_data = {
    'kw' : word,
}
headers = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763',
}
request = urllib.request.Request(url=post_url,headers=headers)
form_data = urllib.parse.urlencode(form_data).encode()
response = urllib.request.urlopen(request,data=form_data)
print(response.read().decode())