import requests
import re
import json

class NeiHan:
    def __init__(self):
        self.url = "https://www.duanzi1.com/category/?1-{}.html"
        self.headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}

    def parse_url(self,url):
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url=url,headers=self.headers,verify=False)
        return response.content.decode()

    def get_response(self,html_str):
        final_result = re.findall("<div class=\"content\"><a(.*?)</a></div>",html_str,re.S)
        return final_result

    def save_result(self,result):
        with open("neihan.txt","a",encoding="utf-8") as fp:
            for final_result in result:
                fp.write(json.dumps(final_result,ensure_ascii=False))
                fp.write("\n")

    def run(self):
        start_page = int(input("请输入开始页码:"))
        end_page = int(input("请输入结束页码:"))
        for page in range(start_page,end_page + 1):
            print("开始下载第%s页" %page)
            url = self.url.format(page)
            html_str = self.parse_url(url)
            result = self.get_response(html_str)
            self.save_result(result)
            print("结束下载第%s页" %page)

if __name__ == '__main__':
    neihan = NeiHan()
    neihan.run()