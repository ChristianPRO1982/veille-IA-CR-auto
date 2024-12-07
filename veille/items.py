# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class VeilleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class AiToolItem(scrapy.Item):
    category = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    tags = scrapy.Field()
    link = scrapy.Field()
    type = scrapy.Field()
    date = scrapy.Field()
    final_url = scrapy.Field()
    