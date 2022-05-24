import scrapy
from selenium import webdriver
n=1
class G1Spider(scrapy.Spider):
    name = 'g1'
    allowed_domains = ['g1.globo.com']
    start_urls = ['https://g1.globo.com/']

    def parse(self, response):
        
        pass

    def parse(self, response):
        global n
        # follow links to news pages
        for page in response.xpath('//div/div[2]/div/div/a/@href').getall():
            yield response.follow(page, self.parse_noticia)

        # follow pagination links
        n += 1
        if n <= 2000:
            next_page = ("https://g1.globo.com/politica/index/feed/pagina-%d.ghtml" % (n))
            yield response.follow(next_page, self.parse)

    def parse_noticia(self, response):
        yield {
            'data': response.xpath('//time/text()')[0].get(),
            'titulo': response.xpath('//h1/text()')[2].get(),
            'link': response.url,
            }
