# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy



class AiToolItem(scrapy.Item):
    category = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    type = scrapy.Field()
    inner_url = scrapy.Field()
    outer_url = scrapy.Field()
    date = scrapy.Field()


class AiToolConcatItem(scrapy.Item):
    id = scrapy.Field()
    category = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    tags = scrapy.Field()
    type = scrapy.Field()
    inner_url = scrapy.Field()
    outer_url = scrapy.Field()
    final_url = scrapy.Field()
    date = scrapy.Field()
    prossed = scrapy.Field()
