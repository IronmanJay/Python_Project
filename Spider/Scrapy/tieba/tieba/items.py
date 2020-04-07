# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TiebaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    标题 = scrapy.Field()
    回复数 = scrapy.Field()
    详情页链接 = scrapy.Field()
    用户名称 = scrapy.Field()
    图片 = scrapy.Field()
    文字 = scrapy.Field()
