import scrapy
import sqlite3
from veille.items import AiToolConcatItem
from veille.spiders.utils import common_headers



common_headers = common_headers()


class TagsSpider(scrapy.Spider):
    name = "tags"
    allowed_domains = ["www.aixploria.com"]


    def start_requests(self):
        conn = sqlite3.connect('ai_tools.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, inner_url FROM ai_tools_concat")
        self.rows = cursor.fetchall()
        conn.close()

        for row in self.rows:
            yield scrapy.Request(url=row[1], meta={"id": row[0]})
            break


    def parse(self, response):
        item = AiToolConcatItem()

        tags = response.css('div.entry-categories span::attr(data-title)').getall()

        item["id"] = response.meta["id"]
        item["tags"] = "|".join(tags)

        yield item
