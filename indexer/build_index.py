import os
import json
import sys
import re
import logging
from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, ID
from whoosh.analysis import StemmingAnalyzer, NgramWordAnalyzer

# Set up logging
logging.basicConfig(level=logging.INFO, 
                   format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def normalize_text(text):
    """Normalize text by converting to lowercase and removing punctuation."""
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    text = re.sub(r'[^\w\s]', ' ', text)
    # Replace multiple spaces with a single space
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def validate_json_file(file_path):
    """Validate that the JSON file exists and contains valid JSON data."""
    if not os.path.exists(file_path):
        logger.error(f"Data file not found: {file_path}")
        return False
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            file_content = f.read()
            
            # Print a preview of the file content for debugging
            logger.info(f"File content preview: {file_content[:100]}...")
            
            # Try to parse the JSON
            data = json.loads(file_content)
            
            # Check if the data is a list and not empty
            if not isinstance(data, list):
                logger.error(f"JSON data is not a list. Type: {type(data)}")
                return False
            
            if len(data) == 0:
                logger.error("JSON data is an empty list.")
                return False
            
            logger.info(f"JSON validation successful. Found {len(data)} articles.")
            return True
            
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in {file_path}: {str(e)}")
        logger.error(f"Content causing the error: {file_content[:200]}")
        return False
    except Exception as e:
        logger.error(f"Error reading {file_path}: {str(e)}")
        return False

def build_index():
    """Build a search index from the data.json file."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_file = os.path.join(os.path.dirname(current_dir), "data", "data.json")
    index_dir = os.path.join(current_dir, "index")
    
    # Validate the JSON file
    if not validate_json_file(data_file):
        logger.error("JSON validation failed. Cannot build index.")
        return False
    
    try:
        # Create the schema with analyzers optimized for Turkish text
        # Use NgramWordAnalyzer for partial word matching
        title_analyzer = NgramWordAnalyzer(minsize=2, maxsize=4)
        content_analyzer = NgramWordAnalyzer(minsize=2, maxsize=4)
        
        schema = Schema(
            title=TEXT(stored=True, analyzer=title_analyzer),
            url=ID(stored=True),
            content=TEXT(stored=True, analyzer=content_analyzer),
            category=TEXT(stored=True)
        )
        
        # Create the index directory if it doesn't exist
        if not os.path.exists(index_dir):
            os.makedirs(index_dir)
            logger.info(f"Created index directory: {index_dir}")
        
        # Create the index
        ix = create_in(index_dir, schema)
        writer = ix.writer()
        
        # Read the data from the JSON file
        with open(data_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Add documents to the index
        for article in data:
            writer.add_document(
                title=article.get("title", ""),
                url=article.get("url", ""),
                content=article.get("content", ""),
                category=article.get("category", "")
            )
            logger.info(f"Indexed article: {article.get('title', '')}")
        
        # Commit the changes
        writer.commit()
        
        logger.info(f"Successfully built index with {len(data)} articles.")
        return True
        
    except Exception as e:
        logger.error(f"Error building index: {str(e)}")
        return False

if __name__ == "__main__":
    logger.info("Starting to build the search index...")
    success = build_index()
    if success:
        logger.info("✓ Index built successfully.")
    else:
        logger.error("✗ Failed to build index. Please check the errors above.")
        sys.exit(1) 