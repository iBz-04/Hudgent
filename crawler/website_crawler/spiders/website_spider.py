import scrapy
from website_crawler.items import WebsiteItem

class WebsiteSpider(scrapy.Spider):
    name = "website_spider"
    start_urls = ["https://www.islamveihsan.com/"]
    allowed_domains = ["islamveihsan.com"]

    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)
        
        # Try multiple selector patterns to find articles
        article_links = []
        
        # Pattern 1: Main article links
        links = response.css('h2.entry-title a::attr(href)').getall()
        if links:
            self.logger.info(f"Found {len(links)} articles with pattern 1")
            article_links.extend(links)
            
        # Pattern 2: Featured articles
        links = response.css('article.post a::attr(href)').getall()
        if links:
            self.logger.info(f"Found {len(links)} articles with pattern 2")
            article_links.extend(links)
            
        # Pattern 3: Menu links to categories
        links = response.css('ul.menu a::attr(href)').getall()
        if links:
            self.logger.info(f"Found {len(links)} category links with pattern 3")
            for link in links:
                if 'islamveihsan.com' in link and not link.endswith('/'):
                    yield response.follow(link, self.parse)
        
        # Follow article links
        for article in article_links:
            self.logger.debug(f"Following article link: {article}")
            yield response.follow(article, self.parse_article)
        
        # Pagination
        next_page = response.css('a.next::attr(href), a.next.page-numbers::attr(href)').get()
        if next_page:
            self.logger.info(f"Found next page: {next_page}")
            yield response.follow(next_page, self.parse)

    def parse_article(self, response):
        self.logger.info(f"Parsing article: {response.url}")
        item = WebsiteItem()
        
        # Try multiple selector patterns for title
        title = response.css('h1.entry-title::text, h1.post-title::text').get()
        if title:
            item['title'] = title.strip()
        else:
            self.logger.warning(f"No title found for {response.url}")
            item['title'] = "No title found"
            
        item['url'] = response.url
        
        # Try multiple selector patterns for content
        content = response.css('div.entry-content p::text, div.post-content p::text, article p::text').getall()
        if content:
            item['content'] = ' '.join(content).strip()
        else:
            self.logger.warning(f"No content found for {response.url}")
            item['content'] = "No content found"
            
        # Try multiple selector patterns for category
        category = response.css('span.cat-links a::text, div.breadcrumb a:last-child::text, .breadcrumb span:last-child span::text').get()
        if category:
            item['category'] = category.strip()
        else:
            self.logger.warning(f"No category found for {response.url}")
            item['category'] = "Uncategorized"
            
        self.logger.info(f"Extracted item: {item}")
        return item 