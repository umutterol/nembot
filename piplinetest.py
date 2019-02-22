import json

from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy import log, signals
from scrapy.utils.project import get_project_settings
from spiderQueen import TankSpider


class MyPipeline(object):
    def process_item(self, item, spider):
        results.append(dict(item))

results = []
def spider_closed(spider):
    print(results)

spider = TankSpider()
settings = get_project_settings()
settings.overrides['ITEM_PIPELINES'] = {'__main__.MyPipeline': 1}
crawler = Crawler(settings)

crawler.signals.connect(spider_closed, signal=signals.spider_closed)
crawler.configure()
crawler.crawl(spider)

# start crawling
crawler.start()
log.start()
reactor.run() 