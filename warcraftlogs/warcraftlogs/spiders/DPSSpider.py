# -*- coding: utf-8 -*-
import scrapy


class DPSSpider(scrapy.Spider):
    name = 'DPSSpider'
    allowed_domains = ['https://www.warcraftlogs.com/rankings/guild-rankings-for-zone/255536/dps/21/0/4/10/1/Any/Any/rankings/historical/0/best/0/0']
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