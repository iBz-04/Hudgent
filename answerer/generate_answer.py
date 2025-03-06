import openai
from config.config import OPENAI_API_KEY

def generate_answer(question, context):
    openai.api_key = OPENAI_API_KEY
    
    prompt = f"""
    Based on the following Islamic content from islamveihsan.com:
    {context}
    
    Answer this question: {question}
    
    Provide a detailed answer with references to Quranic verses and Hadith where appropriate.
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "user",
            "content": prompt
        }]
    )
    
    return response.choices[0].message['content'].strip() 