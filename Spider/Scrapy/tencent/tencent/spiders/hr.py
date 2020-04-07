# -*- coding: utf-8 -*-
import scrapy

class HrSpider(scrapy.Spider):
    name = 'hr'
    allowed_domains = ['tencent.com']
    start_urls = ['https://careers.tencent.com/search.html']

    def parse(self, response):
        tr_list = response.xpath("//div[@class='recruit-list']")
        for tr in tr_list:
            item = {}
            item["title"] = tr.xpath(".//a/h4/text()").extract_first()
            item["position"] = tr.xpath(".//a/p/span[1]/text()").extract_first()
            item["place"] = tr.xpath(".//a/p/span[2]/text()").extract_first()
            item["kind"] = tr.xpath(".//a/p/span[3]/text()").extract_first()
            item["describe"] = tr.xpath(".//a/p[2]/text()").extract_first()
            yield item
        #找到下一页的url地址
        next_url = response.xpath("//div[@class='page-number']//li[10]").extract_first()
        if next_url != "javascript:;":
            next_url = "https://careers.tencent.com/" + next_url
            yield scrapy.Request(
                next_url,
                callback=self.parse()
            )