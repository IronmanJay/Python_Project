# -*- coding: utf-8 -*-
import scrapy
from Travel.items import TravelItem

class TravelSpider(scrapy.Spider):
    name = 'travel'
    allowed_domains = ['https://www.cncn.com']
    start_urls = ['https://www.cncn.com/top/']

    def parse(self, response):
        allHref = response.xpath("//div[@class='tit']/span/a")
        for Href in allHref:
            href = Href.xpath("./@href").extract_first()
            print(href)
            yield scrapy.Request(
                href,
                callback=self.parseDetail,
                dont_filter=True
            )

    def parseDetail(self,response):
        datas = response.xpath("//div[@class='resizeimg4']/div/li/a")
        for data in datas:
            item = TravelItem()
            item['name'] = data.xpath("./text()").extract()[0]
            item['link'] = data.xpath("./@href").extract()[0]
            yield item

