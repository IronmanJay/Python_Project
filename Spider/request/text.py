import requests
import json
import sys

class BaiDuFanYi:
    def __init__(self,trans_str):
        self.trans_str = trans_str
        self.lang_detect_url = "https://fanyi.baidu.com/langdetect"
        self.trans_url = "https://fanyi.baidu.com/basetrans"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Mobile Safari/537.36"}

    def parse_url(self, url, data):
        resquest = requests.get(url,data=data,headers=self.headers)
        response = requests.post(resquest)
        return json.loads(response.content.decode())

    def get_ret(self, dict_response):
        print(dict_response)
        exit()
        ret = dict_response["trans"][0]["dst"]
        print("result is ", ret)

    def run(self):
        lang_detect_data = {"query": self.trans_str}
        lang = self.parse_url(self.lang_detect_url, lang_detect_data)["lan"]
        trans_data = {"query": self.trans_str, "from": "zh", "to": "en","token": "6e26908a638badf342c2d7264028031e","sign": "54706.276099"} if lang == "zh" else {
            "query": self.trans_str, "from": "en", "to": "zh","token": "6e26908a638badf342c2d7264028031e","sign": "54706.276099"}
        dict_response = self.parse_url(self.trans_url, trans_data)
        self.get_ret(dict_response)


if __name__ == '__main__':
    trans_str = input("请输入想翻译的内容:")
    # trans_str = sys.argv[1]
    baidu_fanyi = BaiDuFanYi(trans_str)
    baidu_fanyi.run()