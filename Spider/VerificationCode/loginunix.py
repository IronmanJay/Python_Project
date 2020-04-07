import urllib.request
import urllib.parse
url = 'http://account.chinaunix.net/login/login'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763',
}
formdata = {
    'username' : 'IronmanJay',
    'password' : 'mimanibuzhidao',
    '_token' : 'blwjCEDtrCbRWrtsfg7aoDRwLuFiQUsf2D6N7eZ2',
    '_t' : '1565005390645',
}
formdata = urllib.parse.urlencode(formdata).encode()
request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request,data=formdata)
with open('unix.html','wb') as fp:
    fp.write(response.read())