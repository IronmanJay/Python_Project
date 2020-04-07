import urllib.request
import urllib.parse
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
url = 'http://www.baidu.com/'
# response = urllib.request.urlopen(url)
# print(response.read().decode())
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763',
}
request = urllib.request.Request(url = url,headers = headers)
response = urllib.request.urlopen(request)
print(response.read().decode())