import scrapy


class InfoAixploraSpider(scrapy.Spider):
    name = "info_aixplora"
    allowed_domains = ["www.aixploria.com"]
    start_urls = ["https://www.aixploria.com/categories-ai/"]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
                'Accept-Language': 'fr',
            })


    def parse(self, response):
        movies = response.css('li.ipc-metadata-list-summary-item')
