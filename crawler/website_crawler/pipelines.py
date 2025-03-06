import json
import os
from scrapy.exporters import JsonItemExporter

class JsonWriterPipeline:
    def open_spider(self, spider):
        # Create data directory if it doesn't exist
        data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '..', 'data')
        os.makedirs(data_dir, exist_ok=True)
        
        # Use absolute path to ensure file is created in the right location
        data_file = os.path.join(data_dir, 'data.json')
        spider.logger.info(f"Writing output to {data_file}")
        
        self.file = open(data_file, 'wb')
        self.exporter = JsonItemExporter(self.file)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
        spider.logger.info("Pipeline closed successfully")

    def process_item(self, item, spider):
        spider.logger.debug(f"Processing item: {item}")
        self.exporter.export_item(item)
        return item 