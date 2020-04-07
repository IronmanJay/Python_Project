# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class CfSpider(CrawlSpider):
    name = 'cf'
    allowed_domains = ['circ.gov.cn']
    start_urls = ['http://www.cbirc.gov.cn/cn/list/9103/910305/ybjhcf/1.html']
    # start_urls = ['http://www.circ.gov.cn/cn/web/site0/tab5240/module14430/page1.htm']

    #定义提取url地址规则
    rules = (
        #LinkExtractor 连接提取器，提取url地址
        #callback 提取出来的url地址的response会交给callback处理
        #follow 当前url地址的响应是否重新经过rules来提取url地址
        Rule(LinkExtractor(restrict_xpaths=u'//table[@width="96%"]/tr/td//a/@href'), callback='parse_item'),
        # Rule(LinkExtractor(allow=r'/cn/doc/9103/910305/ybjhcf/\d+\.html'), follow=True),
        # Rule(LinkExtractor(allow=r'/web/site0/tab5240/info\d+\.htm'),
        #      callback='parse_item'),
    )
    #parse函数有特殊功能，不能定义
    def parse_item(self, response):
        item = {}
        item["title"] = response.xpath("//table[@width='90%']/tr[3]/td/div/p[1]/span/text()").extract_first() + response.xpath("//table[@width='90%']/tr[3]/td/div/p[2]/span/text()").extract_first() + response.xpath("//table[@width='90%']/tr[3]/td/div/p[3]/span").extract_first()
        item["info"] = response.xpath("//table[@width='90%']/tr[1]/td/text()").extract_first()
        # item["title"] = re.findall("<!--TitleStart-->(.?)<!--TitleEnd-->",response.body.decode())[0]
        # item["publish_date"] = re.findall("发布时间:(20\d{2}-\d{2}-\d{2})", response.body.decode())[0]
        print(item)