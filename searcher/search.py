import os
import json
import re
from whoosh.index import open_dir
from whoosh.qparser import QueryParser, OrGroup
from whoosh.query import Term, Or
import logging

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

def search_index(question):
    """Search the index for relevant documents based on the question."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    index_dir = os.path.join(os.path.dirname(current_dir), "indexer", "index")
    
    # Check if index directory exists
    if not os.path.exists(index_dir):
        logger.error(f"Index directory not found: {index_dir}")
        return []
    
    try:
        # Open the index
        ix = open_dir(index_dir)
        
        # Normalize the question
        normalized_question = normalize_text(question)
        logger.info(f"Searching for: '{question}'")
        logger.info(f"Normalized question: '{normalized_question}'")
        
        # Extract search terms
        search_terms = normalized_question.split()
        logger.info(f"Search terms: {search_terms}")
        
        results = []
        
        with ix.searcher() as searcher:
            # Try different search approaches
            
            # Approach 1: Standard query parser with OR operator
            query_parser = QueryParser("content", ix.schema, group=OrGroup)
            query = query_parser.parse(normalized_question)
            
            search_results = searcher.search(query, limit=5)
            
            if len(search_results) > 0:
                logger.info(f"Found {len(search_results)} results with standard query")
                for result in search_results:
                    results.append({
                        "title": result["title"],
                        "content": result["content"],
                        "url": result.get("url", ""),
                        "score": result.score
                    })
                return results
            
            logger.info("No results with standard query, trying term-by-term search...")
            
            # Approach 2: Search for individual terms
            term_queries = []
            for field in ["title", "content", "category"]:
                for term in search_terms:
                    if len(term) >= 2:  # Only search for terms with at least 2 characters
                        term_queries.append(Term(field, term))
            
            if term_queries:
                or_query = Or(term_queries)
                search_results = searcher.search(or_query, limit=5)
                
                if len(search_results) > 0:
                    logger.info(f"Found {len(search_results)} results with term-by-term search")
                    for result in search_results:
                        results.append({
                            "title": result["title"],
                            "content": result["content"],
                            "url": result.get("url", ""),
                            "score": result.score
                        })
                    return results
            
            # Approach 3: Wildcard search for partial matches
            for field in ["title", "content", "category"]:
                for term in search_terms:
                    if len(term) >= 3:  # Only use wildcards for terms with at least 3 characters
                        # Create a wildcard query manually
                        wildcard_query = f"{field}:{term}*"
                        query = query_parser.parse(wildcard_query)
                        search_results = searcher.search(query, limit=5)
                        
                        if len(search_results) > 0:
                            logger.info(f"Found {len(search_results)} results with wildcard search for '{term}*'")
                            for result in search_results:
                                results.append({
                                    "title": result["title"],
                                    "content": result["content"],
                                    "url": result.get("url", ""),
                                    "score": result.score
                                })
                            return results
        
        logger.info("No matching content found for your question.")
        return []
    
    except Exception as e:
        logger.error(f"Error searching index: {str(e)}")
        return []

def get_relevant_content(question):
    """Get relevant content for the question."""
    results = search_index(question)
    
    if not results:
        return "No matching content found for your question."
    
    # Format the results
    formatted_results = []
    for i, result in enumerate(results, 1):
        formatted_result = f"Document {i}:\nTitle: {result['title']}\n"
        formatted_result += f"Content: {result['content']}\n"
        if result.get("url"):
            formatted_result += f"Source: {result['url']}\n"
        formatted_results.append(formatted_result)
    
    return "\n".join(formatted_results) 