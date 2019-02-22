import scrapy
from scrapy.crawler import CrawlerProcess

class DPSSpider(scrapy.Spider):
    name = 'DPSSpider'

    allowed_domains = ['https://www.warcraftlogs.com/']
    start_urls = ['https://www.warcraftlogs.com/rankings/guild-rankings-for-zone/255536/dps/21/0/4/10/1/Any/Any/rankings/historical/0/best/0/0']

    def parse(self, response):
        for char in response.xpath('//div[contains(@class,\'character-metric-container\')]//div[2]//table[1]//tbody[1]/tr'):
            yield{
                'name': char.xpath('.//td[1]/a[1]/text()').extract_first().strip(),
                'average': char.xpath('.//td[2]/text()').extract_first().strip(),
                'CoL': char.xpath('.//td[3]/text()').extract_first().strip(),
                'JFM': char.xpath('.//td[4]/text()').extract_first().strip(),
                'Grong': char.xpath('.//td[5]/text()').extract_first().strip(),
                'Opul': char.xpath('.//td[6]/text()').extract_first().strip(),
                'CoC': char.xpath('.//td[7]/text()').extract_first().strip(),
                'Rasta': char.xpath('.//td[8]/text()').extract_first().strip(),
                'Mecha': char.xpath('.//td[9]/text()').extract_first().strip(),
                'Block': char.xpath('.//td[10]/text()').extract_first().strip(),
                'Jaina': char.xpath('.//td[11]/text()').extract_first().strip(),
                'AllStar': char.xpath('.//td[12]/text()').extract_first().strip()
            }
class TankSpider(scrapy.Spider):
    name = 'tankSpider'
    allowed_domains = ['https://www.warcraftlogs.com/']
    start_urls = ['https://www.warcraftlogs.com/rankings/guild-rankings-for-zone/255536/dps/21/0/4/10/1/Any/Any/rankings/historical/0/best/0/0/']

    def parse(self, response):
        for char in response.xpath('//div[contains(@class,\'character-metric-container\')]//div[4]//table[1]//tbody[1]/tr'):
            yield{
                'name': char.xpath('.//td[1]/a[1]/text()').extract_first().strip(),
                'average': char.xpath('.//td[2]/text()').extract_first().strip(),
                'CoL': char.xpath('.//td[3]/text()').extract_first().strip(),
                'JFM': char.xpath('.//td[4]/text()').extract_first().strip(),
                'Grong': char.xpath('.//td[5]/text()').extract_first().strip(),
                'Opul': char.xpath('.//td[6]/text()').extract_first().strip(),
                'CoC': char.xpath('.//td[7]/text()').extract_first().strip(),
                'Rasta': char.xpath('.//td[8]/text()').extract_first().strip(),
                'Mecha': char.xpath('.//td[9]/text()').extract_first().strip(),
                'Block': char.xpath('.//td[10]/text()').extract_first().strip(),
                'Jaina': char.xpath('.//td[11]/text()').extract_first().strip(),
                'AllStar': char.xpath('.//td[12]/text()').extract_first().strip()
            }

class HealSpider(scrapy.Spider):
    name = 'healSpider'
    allowed_domains = ['https://www.warcraftlogs.com/']
    start_urls = ['https://www.warcraftlogs.com/rankings/guild-rankings-for-zone/255536/hps/21/0/4/10/1/Any/Any/rankings/historical/0/best/0/0']

    def parse(self, response):
        for char in response.xpath('//div[@class=\'character-metric-container\']//div[2]//table[1]//tbody[1]/tr'):
            yield{
                'name': char.xpath('.//td[1]/a[1]/text()').extract_first().strip(),
                'average': char.xpath('.//td[2]/text()').extract_first().strip(),
                'CoL': char.xpath('.//td[3]/text()').extract_first().strip(),
                'JFM': char.xpath('.//td[4]/text()').extract_first().strip(),
                'Grong': char.xpath('.//td[5]/text()').extract_first().strip(),
                'Opul': char.xpath('.//td[6]/text()').extract_first().strip(),
                'CoC': char.xpath('.//td[7]/text()').extract_first().strip(),
                'Rasta': char.xpath('.//td[8]/text()').extract_first().strip(),
                'Mecha': char.xpath('.//td[9]/text()').extract_first().strip(),
                'Block': char.xpath('.//td[10]/text()').extract_first().strip(),
                'Jaina': char.xpath('.//td[11]/text()').extract_first().strip(),
                'AllStar': char.xpath('.//td[12]/text()').extract_first().strip()
            }
class ItemSpider(scrapy.Spider):
    name = 'ItemSpider'
    allowed_domains = ['https://www.warcraftlogs.com/']
    start_urls = ['https://www.warcraftlogs.com/rankings/guild-rankings-for-zone/255536/hps/21/0/4/10/1/Any/Any/rankings/historical/0/best/0/0']
    
    def parse(self, response):
        for char in response.xpath('//div[@class=\'character-metric-container\']//div[2]//table[1]//tbody[1]/tr'):
            yield{
                'name': char.xpath('.//td[1]/a[1]/text()').extract_first().strip(),
                'average': char.xpath('.//td[2]/text()').extract_first().strip(),
                'CoL': char.xpath('.//td[3]/text()').extract_first().strip(),
                'JFM': char.xpath('.//td[4]/text()').extract_first().strip(),
                'Grong': char.xpath('.//td[5]/text()').extract_first().strip(),
                'Opul': char.xpath('.//td[6]/text()').extract_first().strip(),
                'CoC': char.xpath('.//td[7]/text()').extract_first().strip(),
                'Rasta': char.xpath('.//td[8]/text()').extract_first().strip(),
                'Mecha': char.xpath('.//td[9]/text()').extract_first().strip(),
                'Block': char.xpath('.//td[10]/text()').extract_first().strip(),
                'Jaina': char.xpath('.//td[11]/text()').extract_first().strip(),
                'AllStar': char.xpath('.//td[12]/text()').extract_first().strip()
            }
class wChar(scrapy.Item):
    name = scrapy.Field()
    average = scrapy.Field()
    col = scrapy.Field()
    jfm = scrapy.Field()
    grong = scrapy.Field()
    opul = scrapy.Field()
    coc = scrapy.Field()
    rasta = scrapy.Field()
    mecha = scrapy.Field()
    block = scrapy.Field()
    jaina = scrapy.Field()
    allstart = scrapy.Field()


class SpiderQueen():
    
    def DPSSpiderCrawl(self):
        crawler = CrawlerProcess({
            'USER_AGENT': 'Mozilla/5.0',
            'FEED_FORMAT': 'json',
            'FEED_URI': 'dps.json',
            'FEED_EXPORT_ENCODING' : 'utf-8',
        })
        crawler.crawl(DPSSpider)
        crawler.start()

    def TankSpiderCrawl(self):
        crawler = CrawlerProcess({
            'USER_AGENT': 'Mozilla/5.0',
            'FEED_FORMAT': 'json',
            'FEED_URI': 'tdps.json',
            'FEED_EXPORT_ENCODING' : 'utf-8',
        })
        crawler.crawl(TankSpider)
        crawler.start()
    
    def HealSpiderCrawl(self):
        crawler = CrawlerProcess({
            'USER_AGENT': 'Mozilla/5.0',
            'FEED_FORMAT': 'json',
            'FEED_URI': 'hps.json',
            'FEED_EXPORT_ENCODING' : 'utf-8',
        })
        crawler.crawl(HealSpider)
        crawler.start()
    def Queen(self):
        crawler = CrawlerProcess({
            'USER_AGENT': 'Mozilla/5.0',
            'FEED_FORMAT': 'json',
            'FEED_URI': 'hps.json',
            'FEED_EXPORT_ENCODING' : 'utf-8',
            'LOG_LEVEL':'WARNING',
        })
        crawler.crawl(HealSpider)
        crawler = CrawlerProcess({
            'USER_AGENT': 'Mozilla/5.0',
            'FEED_FORMAT': 'json',
            'FEED_URI': 'tdps.json',
            'FEED_EXPORT_ENCODING' : 'utf-8',
            'LOG_LEVEL':'WARNING',
        })
        crawler.crawl(TankSpider)
        crawler = CrawlerProcess({
            'USER_AGENT': 'Mozilla/5.0',
            'FEED_FORMAT': 'json',
            'FEED_URI': 'dps.json',
            'FEED_EXPORT_ENCODING' : 'utf-8',
            'LOG_LEVEL':'WARNING',
        })
        crawler.crawl(DPSSpider)
        crawler.start()
