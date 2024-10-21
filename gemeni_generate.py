import google.generativeai as genai

# Configure the GEMINI LLM
genai.configure(api_key='')#insert api key
model = genai.GenerativeModel('gemini-pro')

#basic generation
def generate_text(prompt):
    response = model.generate_content(prompt)
    return response.text
