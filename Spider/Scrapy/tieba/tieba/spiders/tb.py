# -*- coding: utf-8 -*-
import scrapy
from tieba.items import TiebaItem

class TbSpider(scrapy.Spider):
    name = 'tb'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['https://tieba.baidu.com/f?kw=%C0%EE%D2%E3&fr=ala0&tpl=5']

    def parse(self, response):
        li_list = response.xpath("//div[@id='pagelet_frs-list/pagelet/thread_list']/ul/li")
        for li in li_list:
            item = TiebaItem()
            item["标题"] = li.xpath("./div/div[2]/div/div/a/text()").extract_first()
            item["回复数"] = li.xpath("./div/div[1]/span/text()").extract_first()
            item["详情页链接"] = li.xpath("./div/div[2]/div/div/a/@href").extract_first()
            item["详情页链接"] = ["https://tieba.baidu.com" + i for i in item["详情页链接"]]
            yield scrapy.Request(
                item["详情页链接"],
                callback = self.get_next_page,
                mate = {"item" : item}
            )
            next_url = response.xpath("//div[@class='thread_list_bottom clearfix']/div/a[10]/@href").extract_first()
            yield scrapy.Request(
                next_url,
                callback = self.parse
            )

    def get_next_page(self,response):
        item = response.mate["item"]
        item["用户名称"] = response.xpath("//ul[@class='p_author']/li[3]/a/text()").extract_first()
        item["文字"] = response.xpath("//div[@class='d_post_content_main']/div/cc/div[2]/text()").extract()
        item["图片"] = response.xpath("//div[@class='p_content']/cc/div[2]/img/@src").extract()
        yield item