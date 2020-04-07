import urllib.request
import urllib.parse
post_url = 'https://fanyi.baidu.com/v2transapi'
word = 'wolf'
formdata = {
    'from':'en',
    'to':'zh',
    'query':word,
    'transtype':'realtime',
    'simple_means_flag':'3',
    'sign':	'275695.55262',
    'token':'cf035444a4029af3f16e173c917b387c',
}
headers = {
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763',
    # 'Accept': '*/*',
    'Accept-Language': 'zh-CN',
    # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Host': 'fanyi.baidu.com',
    # 'Content-Length': '120',
    'DNT': '1',
    # 'Connection': 'Keep-Alive',
    # 'Cache-Control': 'no-cache',
    'Cookie': 'Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1564233915; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; SOUND_PREFER_SWITCH=1; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; FANYI_WORD_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1564233620,1564233736,1564233915; SOUND_SPD_SWITCH=1; REALTIME_TRANS_SWITCH=1; HISTORY_SWITCH=1; delPer=0; H_PS_PSSID=1435_21118_29520_28518_29099_29568_28836_29221_29072_22160; PSINO=7; ZD_ENTRY=baidu; BDRCVFR[bLbo9QmdyQn]=mk3SLVN4HKm; BAIDUID=378E9F90EA7DA235765CB2AA8EA86344:FG=1; BIDUPSID=378E9F90EA7DA235765CB2AA8EA86344; PSTM=1564233606; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; yjs_js_security_passport=4ab92249c51b385bb196333ce68ac391596a5710_1564233914_js; locale=zh',
}
request = urllib.request.Request(url = post_url,headers = headers)
formdata = urllib.parse.urlencode(formdata).encode()
response = urllib.request.urlopen(request,formdata)
print(response.read().decode())