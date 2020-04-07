import requests
url = 'https://cn.bing.com/tlookupv3?isVertical=1&&IG=B786A5025AF7401C82D3061609A52594&IID=translator.5028.9'
formdata = {
    'from': 'en',
    'to': 'zh-Hans',
    'text': 'lion',
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763',
}
r = requests.post(url=url,headers=headers,data=formdata)
print(r.json())