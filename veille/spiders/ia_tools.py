import scrapy


class IaToolsSpider(scrapy.Spider):
    name = "ia_tools"
    allowed_domains = ["www.aixploria.com"]
    start_urls = ["https://www.aixploria.com"]

    def parse(self, response):
        pass
