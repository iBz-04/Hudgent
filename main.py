import os
import openai
from searcher.search import get_relevant_content

def get_api_key():
    """Get the OpenAI API key from environment variable or user input."""
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        api_key = input("Please enter your OpenAI API key: ")
        os.environ["OPENAI_API_KEY"] = api_key
    return api_key

def ask_question(question, context):
    """Ask a question to the OpenAI API."""
    client = openai.OpenAI(api_key=get_api_key())
    
    try:
        # Create the prompt with the context
        prompt = f"""
        You are an Islamic knowledge assistant. Use ONLY the following information to answer the question.
        If the information is not in the provided context, say "I don't have enough information to answer that question."
        
        Context:
        {context}
        
        Question: {question}
        """
        
        # Call the OpenAI API with the new client.chat.completions.create method
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful Islamic knowledge assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        # Extract the answer from the response
        answer = response.choices[0].message.content.strip()
        return answer
    
    except Exception as e:
        return f"An error occurred: {str(e)}\n\nPlease try again."

def main():
    """Main function to run the Q&A system."""
    print("\nIslamic Knowledge Base Q&A System")
    print("=================================")
    print("Type 'exit' to quit the program.\n")
    
    while True:
        # Get the user's question
        question = input("\nEnter your question about Islamic topics: ")
        
        # Check if the user wants to exit
        if question.lower() in ["exit", "quit", "q"]:
            print("Thank you for using the Islamic Knowledge Base Q&A System. Goodbye!")
            break
        
        # Get relevant content for the question
        context = get_relevant_content(question)
        
        # If no relevant content is found, inform the user
        if context == "No matching content found for your question.":
            print("\n" + context)
            continue
        
        # Ask the question to the OpenAI API
        answer = ask_question(question, context)
        
        # Print the answer
        print("\nAnswer:")
        print(answer)

if __name__ == "__main__":
    main() 