#coding:utf-8

import scrapy

class SisyItem(scrapy.Item):
    image_urls = scrapy.Field()
    images     = scrapy.Field()
    image_paths= scrapy.Field()
    
