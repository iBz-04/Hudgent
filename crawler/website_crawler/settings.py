import os

BOT_NAME = 'website_crawler'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
ROBOTSTXT_OBEY = False

SPIDER_MODULES = ['website_crawler.spiders']
NEWSPIDER_MODULE = 'website_crawler.spiders'

# Ensure data directory exists
data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '..', 'data')
os.makedirs(data_dir, exist_ok=True)

# Set feed export settings
FEED_FORMAT = 'json'
FEED_URI = os.path.join(data_dir, 'data.json')

ITEM_PIPELINES = {
    'website_crawler.pipelines.JsonWriterPipeline': 300,
}

DOWNLOAD_DELAY = 2
LOG_LEVEL = 'DEBUG'

# Enable or disable downloader middlewares
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
}

# Configure maximum concurrent requests
CONCURRENT_REQUESTS = 1 