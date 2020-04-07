# -*- coding: utf-8 -*-
import scrapy
from YaMaXun.items import YamaxunItem
from copy import deepcopy

class YamaxuntushuSpider(scrapy.Spider):
    name = 'YaMaXunTuShu'
    allowed_domains = ['amazon.cn']
    start_urls = ['https://www.amazon.cn/s/ref=nb_sb_noss_2?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&url=search-alias%3Dstripbooks&field-keywords=']

    def parse(self, response):
        li_list = response.xpath("//div[@class='a-row a-expander-container a-expander-extend-container']/li")
        for li in li_list:
            item = YamaxunItem()
            item["first_href"] = li.xpath("./span/a/@href").extract()
            item["first_href"] = "https://www.amazon.cn".format(item["first_href"])
            yield scrapy.Request(
                item["first_href"],
                callback=self.second,
                meta={"item":deepcopy(item)}
            )

    def second(self,response):
        item = deepcopy(response.meta["item"])
        li_list = response.xpath("//div[@id='mainResults']/ul/li")
        for li in li_list:
            item["second_href"] = li.xpath("./div/div/div/div/div/div/a/@href").extract()
            yield scrapy.Request(
                item["second_href"],
                callback=self.third,
                meta={"item":response.mate["item"]}
            )
        next_url = response.xpath("//div[@class='a-fixed-left-grid-col a-col-right']/div/div/a/@href").extract_first()
        if next_url is not None:
            scrapy.Request(
                next_url,
                callback=self.second
            )

    def third(self,response):
        item = response.meta["item"]
        item["title"] = response.xpath("//div[@id='centerCol']/div/div/h1/span[1]/text()").extract_first()
        item["author"] = response.xpath("//div[@id='centerCol']/div/div[2]/span[1]/a/text()").extract_first()
        item["price"] = response.xpath("//div[@id='tmmSwatches']/ul/li/span/span/span/a/span/span/text()").extract_first()
        item["time"] = response.xpath("//div[@id='ps-content']/div[1]/span[2]/text()").extract_first()
        item["introduction"] = response.xpath("//div[@id='ps-content']/div[2]/div/div/div//text()").extract_first()
        yield item