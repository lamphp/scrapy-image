#coding:utf-8
import scrapy
from scrapy.selector import Selector
from images.items import  SisyItem
import urlparse

class SisySpider(scrapy.Spider):
    name = "sisy"
    allowed_domains = ["www.aitaotu.com"]
    start_urls = [
                "http://www.aitaotu.com/guonei/19181_1.html"
    ]

    def parse(self, response):
        
        urls = [20317]
        i = 1
        while i <= 60:
            for prefix in urls:
                url = 'http://www.aitaotu.com/guonei/'+str(prefix)+'_'+str(i)+'.html'
                yield scrapy.Request(url, callback=self.parse_item) 
            
            i+=1
            
    def parse_item(self, response):
        
        selector = Selector(response).xpath('//p[@align="center"]')
        for sel in selector:
            image_urls = sel.xpath('a/img/@src').extract()
            path = []
            for img in image_urls:
                path.append(urlparse.urlparse(img).path)
            
        item = SisyItem()                             
        item['image_urls'] = image_urls
        item['images']     = path

        return item
