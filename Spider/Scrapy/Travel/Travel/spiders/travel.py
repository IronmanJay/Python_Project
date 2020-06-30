# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
from Travel.items import TravelItem

class TravelSpider(scrapy.Spider):
    name = 'travel'
    allowed_domains = ['www.cncn.com/top/']
    start_urls = ['http://www.cncn.com/top//']

    def parse(self, response):
        data = response.body
        item = TravelItem()
        html = etree.HTML(data)
        names = html.xpath("//ul/li/a/text()")
        links = html.xpath("//ul/li/a/@href")
        for name,link in zip(names,links):
            item['name'] = name
            item['link'] = link
            yield item

