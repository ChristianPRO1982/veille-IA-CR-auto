import scrapy
import csv
from veille.items import AiToolConcatItem
from veille.spiders.utils import common_headers



common_headers = common_headers()


class TagsSpider(scrapy.Spider):
    name = "tags"
    allowed_domains = ["www.aixploria.com"]


    def start_requests(self):
        file_path = 'output/tags.csv'
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                print('id:', row[0], 'url:', row[1])

        # for row in self.rows:
        #     yield scrapy.Request(url=row[1], meta={"id": row[0]})
        #     break


    def parse(self, response):
        # item = AiToolConcatItem()

        # tags = response.css('div.entry-categories span::attr(data-title)').getall()

        # item["id"] = response.meta["id"]
        # item["tags"] = "|".join(tags)

        # yield item
        pass