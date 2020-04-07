import requests
from lxml import etree
from queue import Queue
import threading

class QiuShiBaiKe:
    def __init__(self):
        # self.start_page = start_page
        # self.end_page = end_page
        self.web_name = "糗事百科"
        self.first_url = "http://www.lovehhy.net/Joke/Detail/QSBK/{}"
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362"}
        self.url_queue = Queue()
        self.html_queue = Queue()

    def get_url(self):
        for i in range(1,18):
            self.url_queue.put(self.first_url.format(i))

    def parse_url(self):
        while True:
            url_all = self.url_queue.get()
            response = requests.get(url=url_all,headers=self.headers)
            # return response.content.decode("gbk")
            self.html_queue.put(response.content.decode("gbk"))
            self.url_queue.task_done()

    def get_course(self):
        while True:
            html_str = self.html_queue.get()
            final_result = etree.HTML(html_str)
            a = final_result.xpath("//div[@id='main']/div/div[3]/div/div/h3/a/text()")
            x= "\n".join(a)
            b = final_result.xpath("//div[@id='main']/div/div[3]/div/div/div/text()")
            y= "\n".join(b)
            c = final_result.xpath("//div[@id='main']/div/div[3]/div/div/text()")
            z= "\n".join(c)
            item = {
                         "标题" : x,
                         "内容" : y,
                         "其他内容": z,
                     }
            for key in item:
                print(key + ":" + str(item[key]))
            # for result in html_result:
            #     a = result.xpath("./div/div[3]/div/div/h3/a/text()")
            #     b = result.xpath("./div/div[3]/div/div/div/text()")
            #     c = result.xpath("./div/div[3]/div/div/text()")
            #     d = "\n".join(b)
            #     item = {
            #         "标题" : a,
            #         "内容" : d,
            #         "其他内容": c,
            #     }
            #     items.append(item)
            #     print(items)
            # self.save_course(items)

    def run(self):
        # for page in range(self.start_page, self.end_page + 1):
        #     url = self.first_url.format(page)
        thread_list = []
        t_url = threading.Thread(target=self.get_url())
        thread_list.append(t_url)
        for i in range(20):
            t_parse = threading.Thread(target=self.parse_url())
            thread_list.append(t_parse)
        for i in range(2):
            t_html = threading.Thread(target=self.get_course())
            thread_list.append(t_html)
        for t in thread_list:
            t.setDaemon(True)
            t.start()
        for q in [self.url_queue,self.html_queue,self.parse_url()]:
            q.join()
        print("主线程结束")

if __name__ == '__main__':
    # start_page = int(input("请输入起始页码："))
    # end_page = int(input("请输入结束页码："))
    qiushibaike = QiuShiBaiKe()
    qiushibaike.run()