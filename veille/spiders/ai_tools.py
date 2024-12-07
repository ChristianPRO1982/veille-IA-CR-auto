import scrapy
import json
from veille.items import AiToolItem



common_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Accept-Language': 'fr',
}


class AiToolsSpider(scrapy.Spider):
    name = "ai_tools"
    allowed_domains = ["www.aixploria.com"]
    

    def start_requests(self):
        with open('categories.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Récupérer les liens depuis le JSON
        if 1 == 0:
            entry = data[0]
            url = entry.get('link')
            category = entry.get('category')
            link_text = entry.get('link_text')
            if url:
                yield scrapy.Request(
                    url,
                    headers=common_headers,
                    callback=self.parse,
                    meta={
                        'category': category,
                        'link_text': link_text,
                        }
                    )
        else:
            for entry in data:
                url = entry.get('link')
                category = entry.get('category')
                link_text = entry.get('link_text')
                if url:
                    yield scrapy.Request(
                        url,
                        headers=common_headers,
                        callback=self.parse,
                        meta={
                            'category': category,
                            'link_text': link_text,
                            }
                        )


    def parse(self, response):
        category = response.meta.get('category') + " [" + response.meta.get('link_text') + "]"
        self.logger.info(f"Scraping category page: {response.url} (Category: {category})")

        div_latest_posts = response.css('div.latest-posts:not(.lateday)')

        div_tools = div_latest_posts.css('div.post-item')
        for tool in div_tools:
            item = AiToolItem()
            
            # TYPE : free, freemium, paid
            div_post_thumbnail = tool.css('div.post-thumbnail')
            divs = div_post_thumbnail.css('div')
            div = divs[1]
            span = div.css('span')
            span = span[1]
            span = span.css('span')
            span = span[0]
            item['type'] = span.css('span::text').get()

            # TITLE
            item['title'] = tool.css('a#specialButton::text').get()
            
            # DESCRIPTION
            item['description'] = tool.css('p.post-excerpt::text').get()

            # TAGS
            tags_bloc = tool.css('span.post-category')
            tags = tags_bloc.css('a')
            tags_list = [tag.css('a::text').get() for tag in tags]
            item['tags'] = tags_list
            
            # LINK
            item['link'] = tool.css('a.visit-site-button4::attr(href)').get()

            # CATEGORY
            item['category'] = category

            yield item

        # NEXT PAGE
        next_page = response.css('a.next.page-numbers::attr(href)').get()
        if next_page:
            self.logger.info(f"Next page found: {next_page}")
            yield scrapy.Request(
                url=next_page,
                headers=common_headers,
                callback=self.parse,
                meta=response.meta
            )
    