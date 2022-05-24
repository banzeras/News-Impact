import scrapy


class BrinvestingSpider(scrapy.Spider):
    name = 'brinvesting'
    allowed_domains = ['https://br.investing.com/equities/brazil']
    start_urls = ['http://https://br.investing.com/equities/brazil/']

    def parse(self, response):
        pass
