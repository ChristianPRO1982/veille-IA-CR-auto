import scrapy
import json



common_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Accept-Language': 'fr',
}


class IaToolsSpider(scrapy.Spider):
    name = "ia_tools"
    allowed_domains = ["www.aixploria.com"]
    

    def start_requests(self):
        with open('categories.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Récupérer les liens depuis le JSON
        # entry = data[0]
        # url = entry.get('link')
        # if url:
        #     yield scrapy.Request(url, headers=common_headers, callback=self.parse)
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
            # TYPE : free, freemium, paid
            div_post_thumbnail = tool.css('div.post-thumbnail')
            divs = div_post_thumbnail.css('div')
            div = divs[1]
            span = div.css('span')
            span = span[1]
            span = span.css('span')
            span = span[0]
            type = span.css('span::text').get()

            # TITLE
            title = tool.css('a#specialButton::text').get()
            
            # DESCRIPTION
            description = tool.css('p.post-excerpt::text').get()

            # TAGS
            tags_bloc = tool.css('span.post-category')
            tags = tags_bloc.css('a')
            tags_list = []
            for tag in tags:
                tags_list.append(tag.css('a::text').get())
            
            # LINK
            link = tool.css('a.visit-site-button4::attr(href)').get()

            yield {
                'category': category,
                'title': title,
                'description': description,
                'tags': tags_list,
                'link': link,
                'type': type,
            }