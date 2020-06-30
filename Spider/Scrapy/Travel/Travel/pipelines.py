# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class TravelPipeline(object):

    def process_item(self, item, spider):
        with open("jd.txt",'a',encoding='utf-8') as f:
            f.write(item['name'] + ',')
            f.write(item['link'] + '\n')
        return item

