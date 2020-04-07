# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import re

class YangguangPipeline(object):
    def process_item(self, item, spider):
        item["content"] = self.process_content(item["content"])
        print(item)
        return item
    def process_content(self,content):
        content = [re.sub(r"\xa0|\s","",i)  for i in content]
        content = [i for i in content if len(i) > 0]#去除列表中的空字符串
        return content

