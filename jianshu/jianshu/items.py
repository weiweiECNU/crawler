# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JianshuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    time = scrapy.Field()
    rent = scrapy.Field()
    rent_style = scrapy.Field()
    source = scrapy.Field()
    type = scrapy.Field()
    devices = scrapy.Field()
    address = scrapy.Field()
    text = scrapy.Field()
    # 定义好了爬虫的字段信息。
    
