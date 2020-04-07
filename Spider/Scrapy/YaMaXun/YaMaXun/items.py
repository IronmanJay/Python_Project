# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YamaxunItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    first_href = scrapy.Field()
    second_href = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    price = scrapy.Field()
    time = scrapy.Field()
    introduction = scrapy.Field()
