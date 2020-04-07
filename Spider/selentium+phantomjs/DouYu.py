from selenium import webdriver
import time
from lxml import etree

class DouYu:

    def __init__(self):
        self.url = "https://www.douyu.com/directory/all"
        self.driver = webdriver.Chrome()

    def get_course(self,html):
        source = etree.HTML(html)
        li_list = source.xpath("//ul[@class='layout-Cover-list']/li")
        content_list = []
        for li in li_list:
            item = {}
            item["房间名称:"] = li.xpath("./div/a/div[2]/div[2]/h2/text()")
            item["房间类型:"] = li.xpath("./div/a/div[2]/div[1]/span/text()")
            item["主播名称:"] = li.xpath("./div/a/div[2]/div[1]/h3/text()")
            item["房间热度:"] = li.xpath("./div/a/div[2]/div[2]/span/text()")
            content_list.append(item)
        print(content_list)
        next_url = self.driver.find_elements_by_xpath("//li[@class=' dy-Pagination-next']")
        next_url = next_url[0] if len(next_url) > 0 else None
        return content_list,next_url

    def run(self):
        self.driver.get(self.url)
        html = self.driver.page_source
        content,next_url= self.get_course(html)
        while next_url is not None:
            next_url.click()
            time.sleep(3)
            html = self.driver.page_source
            content,next_url = self.get_course(html)


if __name__ == '__main__':
    douyu = DouYu()
    douyu.run()