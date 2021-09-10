# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AtualizafolhaspItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title      = scrapy.Field()
    text       = scrapy.Field()
    created_at = scrapy.Field()
    link       = scrapy.Field()
    category   = scrapy.Field()
    subcategory = scrapy.Field()
    pass

