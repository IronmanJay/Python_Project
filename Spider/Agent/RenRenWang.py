import urllib.request
import urllib.parse
url = 'http://www.renren.com/971688724/profile'
headers = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763',
        'Cookie': 'jebecookies=eb1547c2-7c3b-416c-933d-b5db3922219c|||||; ick_login=ceb5a6e2-e6aa-4d5f-bdd0-272c176a80e9; _r01_=1; anonymid=jyofe9a4us6om2; depovince=LN; t=715cacf20bb7ac6f4d685c99fdd251104; societyguester=715cacf20bb7ac6f4d685c99fdd251104; id=971688724; xnsid=c2169d56; ver=7.0; loginfrom=null; jebe_key=e6f4c03e-b127-4fbd-95f4-11f1aa991810%7Ced1335f7ca04f5fc9efadb91e04b98ea%7C1564406803211%7C1%7C1564406803687; wp_fold=0; JSESSIONID=abc9XnTBz-DaVcbsn69Ww; jebe_key=e6f4c03e-b127-4fbd-95f4-11f1aa991810%7Ced1335f7ca04f5fc9efadb91e04b98ea%7C1564406803211%7C1%7C1564406803690',
}
request = urllib.request.Request(url = url,headers=headers)
response = urllib.request.urlopen(request)
with open('renren.html','wb') as fp:
    fp.write(response.read())