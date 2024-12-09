import scrapy
import csv
import sqlite3
from veille.items import AiToolConcatItem
from veille.spiders.utils import common_headers



common_headers = common_headers()


class TagsSpider(scrapy.Spider):
    name = "tags"
    allowed_domains = ["www.aixploria.com"]


    def start_requests(self):
        self.conn = sqlite3.connect('output/ai_tools.db')

        file_path = 'output/tags.csv'
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                yield scrapy.Request(url=row[1], meta={"id": row[0]})
                # break


    def parse(self, response):
        item = AiToolConcatItem()

        tags = response.css('div.entry-categories span::attr(data-title)').getall()

        item["id"] = response.meta["id"]
        item["tags"] = "|".join(tags)

        yield item


    def close(self, reason):
        self.conn.commit()
        self.conn.close()