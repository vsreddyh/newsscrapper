# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Section=scrapy.Field()
    Date=scrapy.Field()
    Headline = scrapy.Field()
    Description=scrapy.Field()
    Link=scrapy.Field()
    pass
