# -*- coding: utf-8 -*-
import scrapy
from copy import deepcopy
import re

class SuningSpider(scrapy.Spider):
    name = 'suning'
    allowed_domains = ['suning.com']
    start_urls = ['https://book.suning.com/?safp=d488778a.homepage1.99345513004.47']

    def parse(self, response):
        #大分类分组
        li_list = response.xpath('//div[@class="book-skin"]/div/div/div/div/div/dl')
        for li in li_list:
            item = {}
            item['分类'] = li.xpath('./dt/h3/a/text()').extract_first()
            #小分类分组
            a_list = li.xpath(".//dd/a")
            for a in a_list:
                item['链接'] = a.xpath('./@href').extract_first()
                item['适合年龄'] = a.xpath('./text()').extract_first()
                if item['链接'] is not None:
                    item['链接'] = item['链接']
                    yield scrapy.Request(
                        item['链接'],
                        callback=self.parse_book_list,
                        meta = {'item':deepcopy(item)}
                    )
    def parse_book_list(self,response):
        item = deepcopy(response.meta['item'])
        #图书列表页分组
        li_list = response.xpath('//div[@id="filter-results"]/ul/li')
        for li in li_list:
            item['book_info'] = li.xpath('.//div[@class="res-info"]/p[2]/a').extract_first()
            item['book_img'] = li.xpath('.//div[@class="res-img"]//img/@src').extract_first()
            if item['book_img'] is None:
                item['book_img'] = li.xpath('.//div[@class="res-img"]//img/@src2').extract_first()
            item['book_shop'] = li.xpath('.//div[@class="res-info"]/p[4]/@salesname').extract_first()
            item['book_href'] = li.xpath('.//div[@class="res-info"]/p[2]/a/@href').extract_first()
            item['book_href'] = 'https://' + item['book_href']
            yield scrapy.Request(
                item['book_href'],
                callback=self.parse_book_detail,
                meta = {'item':response.meta['item']}
            )
        #翻页
        page_count = int(re.findall("var pagecount=(.*?);",response.body.decode())[0])
        current_page = int(re.findall("var currentPage=(.*?);",response.body.decode())[0])
        if current_page < page_count:
            next_url = item['s_href'] + '?pageNumber={}&sort=0'.format(current_page + 1)
            yield scrapy.Request(
                next_url,
                callback=self.parse_book_list,
                meta = {'item':item}
            )
    def parse_book_detail(self,response):
        item = response.meta['item']
        #细分到每一本书
        li_list = response.xpath('//div[@class="wrapper proinfo"]/div')
        for li in li_list:
            item['图书名字'] = li.xpath('//div[@class="wrapper proinfo"]/div/div[2]/div/h1/text()').extract_first()
            item['图书老价格'] = li.xpath('//div[@class="proinfo-container clearfix"]/div[2]//div[@class="proinfo-focus clearfix"]/div/dl/dd//del/text()').extract_first()
            item['图书新价格'] = li.xpath('//div[@class="proinfo-container clearfix"]/div[2]//div[@class="proinfo-focus clearfix"]/div/dl[2]/dd//span/text()').extract_first()
            item['作者'] = li.xpath('//div[@class="proinfo-container clearfix"]/div[2]/ul/li[1]/text()').extract_first()
            item['出版社'] = li.xpath('//div[@class="proinfo-container clearfix"]/div[2]/ul/li[2]/text()').extract_first()
            item['出版时间'] = li.xpath('//div[@class="proinfo-container clearfix"]/div[2]/ul/li[3]//span[2]/text()').extract_first()
            print(item)



