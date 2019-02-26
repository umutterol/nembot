import scrapy
from scrapy.crawler import CrawlerProcess
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
import scrapydo

rankings = {"DPS":[],"Heal":[],"TDPS":[]}
class DPSSpider(scrapy.Spider):
    name = 'DPSSpider'

    allowed_domains = ['https://www.warcraftlogs.com/']
    start_urls = ['https://www.warcraftlogs.com/rankings/guild-rankings-for-zone/255536/dps/21/0/4/10/1/Any/Any/rankings/historical/0/best/0/0']
   
    
    def parse(self, response):
        for char in response.xpath('//div[contains(@class,\'character-metric-container\')]//div[2]//table[1]//tbody[1]/tr'):
            char = {
                "name": char.xpath('.//td[1]/a[1]/text()').extract_first().strip(),
                "average": char.xpath('.//td[2]/text()').extract_first().strip(),
                "CoL": char.xpath('.//td[3]/text()').extract_first().strip(),
                "JFM": char.xpath('.//td[4]/text()').extract_first().strip(),
                "Grong": char.xpath('.//td[5]/text()').extract_first().strip(),
                "Opul": char.xpath('.//td[6]/text()').extract_first().strip(),
                "CoC": char.xpath('.//td[7]/text()').extract_first().strip(),
                "Rasta": char.xpath('.//td[8]/text()').extract_first().strip(),
                "Mecha": char.xpath('.//td[9]/text()').extract_first().strip(),
                "Block": char.xpath('.//td[10]/text()').extract_first().strip(),
                "Jaina": char.xpath('.//td[11]/text()').extract_first().strip(),
                "AllStar": char.xpath('.//td[12]/text()').extract_first().strip()
            }
            global rankings
            rankings["DPS"].append(char)

class TankSpider(scrapy.Spider):
    name = 'tankSpider'
    allowed_domains = ['https://www.warcraftlogs.com/']
    start_urls = ['https://www.warcraftlogs.com/rankings/guild-rankings-for-zone/255536/dps/21/0/4/10/1/Any/Any/rankings/historical/0/best/0/0/']
    
    def parse(self, response):
        for char in response.xpath('//div[contains(@class,\'character-metric-container\')]//div[4]//table[1]//tbody[1]/tr'):
            char = {
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
            global rankings
            rankings['TDPS'].append(char)

class HealSpider(scrapy.Spider):
    name = 'healSpider'
    allowed_domains = ['https://www.warcraftlogs.com/']
    start_urls = ['https://www.warcraftlogs.com/rankings/guild-rankings-for-zone/255536/hps/21/0/4/10/1/Any/Any/rankings/historical/0/best/0/0']
    
    def parse(self, response):
        for char in response.xpath('//div[@class=\'character-metric-container\']//div[2]//table[1]//tbody[1]/tr'):
            char = {
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
            global rankings
            rankings["Heal"].append(char)
class SpiderQueen():
    scrapydo.setup()
    global rankings
    rankings = {"DPS":[],"Heal":[],"TDPS":[]}
    def DPSSpiderCrawl(self):
        crawler = CrawlerProcess({
            'USER_AGENT': 'Mozilla/5.0',
            'FEED_FORMAT': 'json',
            'FEED_URI': 'dps.json',
            'FEED_EXPORT_ENCODING' : 'utf-8',
        })
        crawler.crawl(DPSSpider)
        crawler.start()
        return dpsList

    def TankSpiderCrawl(self):
        crawler = CrawlerProcess({
            'USER_AGENT': 'Mozilla/5.0',
        })
        crawler.crawl(TankSpider)
        crawler.start()
    
    def HealSpiderCrawl(self):
        crawler = CrawlerProcess({
            'USER_AGENT': 'Mozilla/5.0',
        })
        crawler.crawl(HealSpider)
        crawler.start()
    def Queen(self):
        
        global rankings
        rankings = {"DPS":[],"Heal":[],"TDPS":[]}
        scrapydo.run_spider(DPSSpider(), settings = {'USER_AGENT': 'Mozilla/5.0',})
        scrapydo.run_spider(TankSpider(), settings = {'USER_AGENT': 'Mozilla/5.0',})
        scrapydo.run_spider(HealSpider(), settings = {'USER_AGENT': 'Mozilla/5.0',})
        return rankings
    
    