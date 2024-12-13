import scrapy
import sqlite3
from veille.spiders.utils import common_headers



common_headers = common_headers()


class InfoAixploraSpider(scrapy.Spider):
    name = "info_aixplora"
    allowed_domains = ["www.aixploria.com"]
    start_urls = ["https://www.aixploria.com/categories-ai/"]


    def start_requests(self):
        self.conn = sqlite3.connect('output/ai_tools.db')

        for url in self.start_urls:
            yield scrapy.Request(url, headers=common_headers)


    def parse(self, response):
        category_groups = response.css('div.categorie-generale-content')
        for category_group in category_groups:
            category = category_group.css('h2::text').get()
            ul_links = category_group.css('ul.categories-associees')
            for link in ul_links.css('a'):
                yield {
                    'category': category,
                    'link': link.attrib['href'],
                    'link_text': link.css('span::text').get(),
                }


    def close_spider(self, spider, reason):
        self.conn.rollback()
        self.conn.close()
        # Logic to disable pipelines if needed
        spider.crawler.engine.close_spider(self, reason)