import os
import sys
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from website_crawler.spiders.website_spider import WebsiteSpider

def main():
    # Ensure we're in the right directory
    print(f"Current working directory: {os.getcwd()}")
    
    # Create data directory if it doesn't exist
    data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
    os.makedirs(data_dir, exist_ok=True)
    print(f"Data directory created/verified: {data_dir}")
    
    # Get the project settings
    settings = get_project_settings()
    print("Settings loaded successfully")
    
    # Create and configure the crawler process
    process = CrawlerProcess(settings)
    print("Adding spider to crawler process...")
    
    # Add the spider to the process
    process.crawl(WebsiteSpider)
    print("Spider added successfully")
    
    # Start the crawling process
    print("Starting the crawler...")
    process.start()
    print("Crawling completed")

if __name__ == "__main__":
    main() 