#coding:utf-8
#scrapy crawl news -s LOG_FILE=scrapy.log

from images.items import SisyItem
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
import scrapy
import time

#下载图片专用
class SisyPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        headers={
            'Referer':'http://www.aitaotu.com',
            'Connection':'keep-alive',
            'Host':'img.aitaotu.cc:8088',
            'Accept-Encoding':'gzip, deflate, sdch'
        }
        if info.spider.name == 'sisy':
            for image_url in item['image_urls']:
                print 'real_image_url:'+image_url
                yield scrapy.Request(url=image_url,headers=headers)
        else:
            pass

    def item_completed(self, results, item, info):
        if info.spider.name == 'sisy':
            image_paths = [x['path'] for ok, x in results if ok]
            if not image_paths:
                raise DropItem("Item contains no images")
            item['image_paths'] = image_paths
            return item       
        
