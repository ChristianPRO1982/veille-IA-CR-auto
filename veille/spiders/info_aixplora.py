import scrapy



common_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Accept-Language': 'fr',
}


class InfoAixploraSpider(scrapy.Spider):
    name = "info_aixplora"
    allowed_domains = ["www.aixploria.com"]
    start_urls = ["https://www.aixploria.com/categories-ai/"]


    def start_requests(self):
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
