import scrapy

class WebsiteItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    content = scrapy.Field()
    category = scrapy.Field() 