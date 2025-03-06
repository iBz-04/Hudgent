import sys
import logging
from searcher.search import search_index

# Set up logging
logging.basicConfig(level=logging.INFO, 
                   format='%(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def test_search():
    """Test the search functionality with sample questions."""
    # Sample questions that should match our data
    test_questions = [
        "İslam'da dua etmenin önemi nedir",
        "Ramazan'da neler yapılır",
        "Abdestte su yutmak orucu bozar mı",
        "Dua",
        "Oruç",
        "Ramazan"
    ]
    
    successful_tests = 0
    
    print("\n====================================================")
    print("TESTING SEARCH FUNCTIONALITY")
    print("====================================================\n")
    
    for question in test_questions:
        print(f"Testing question: '{question}'\n")
        
        results = search_index(question)
        
        if results:
            successful_tests += 1
            print(f"✓ SUCCESS: Found {len(results)} matches for '{question}'")
            print("Matching documents:")
            for i, result in enumerate(results, 1):
                print(f"  {i}. {result['title']} (Score: {result['score']:.2f})")
        else:
            print(f"✗ FAILED: No matches found for '{question}'")
        
        print("\n" + "-" * 50 + "\n")
    
    print("====================================================")
    print(f"Test results: {successful_tests}/{len(test_questions)} successful searches")
    
    if successful_tests == len(test_questions):
        print("✓ All tests passed! The search system is working correctly.")
        return True
    else:
        print(f"✗ {len(test_questions) - successful_tests} tests failed. The search system needs improvement.")
        return False

if __name__ == "__main__":
    print("Starting search system tests...")
    success = test_search()
    if not success:
        sys.exit(1) 