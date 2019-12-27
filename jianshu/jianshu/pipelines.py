# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class JianshuPipeline(object):
    def process_item(self, item, spider):

        fp = open('/Users/apple/Downloads/Code/crawler/todaySydney.txt', 'a+')
        fp.write(item['title']+'\n')
        fp.write(item['time']+'\n')
        fp.write(item['rent']+'\n')
        fp.write(item['rent_style']+'\n')
        fp.write(item['source']+'\n')
        fp.write(item['type']+'\n')
        fp.write(item['devices']+'\n')
        fp.write(item['address']+'\n')
        fp.write(item['text']+'\n')

        return item
