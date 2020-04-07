import json
import urllib.request
import urllib.parse
class BaiDuFanYi:
    def __init__(self,key):
        self.url = "https://fanyi.baidu.com/sug"
        self.key = key
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}
    def run(self):
        data = {
            "kw":self.key
        }
        request = urllib.request.Request(url=self.url,headers=self.headers)
        data = urllib.parse.urlencode(data).encode()
        response = urllib.request.urlopen(request,data=data)
        final_key = json.loads(response.read().decode())
        print("您的结果是%s" %final_key)
key = input("请输入您想翻译的英文单词:")
fanyi = BaiDuFanYi(key)
fanyi.run()