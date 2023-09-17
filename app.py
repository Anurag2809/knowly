from flask import Flask, render_template, request
import openai
import re, os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


app = Flask(__name__)

# Define your OpenAI API key here
api_key = os.getenv('APIKey')

#api_key2 = 

# Initialize the OpenAI API client
openai.api_key = api_key

@app.route('/')
def index():
    return render_template('index.html', search_results=None)  # Initialize search_results as None

@app.route('/search', methods=['POST'])
def search():
    try:
        search_query = request.form.get('search_input')
        selected_language = request.form.get('language-select')
        
        # Define the system message and user message for the OpenAI chat
        search_query = f"Give me 5 useful website links of the Top Articles on the topic {search_query} and also give me 5 website links to articles in the {selected_language} language."
        
        # Create a conversation with system and user messages
        conversation = [
            {"role": "system", "content": "You are a helpful assistant that provides article links and also provide the maximum content which isnt redundant on the topic."},
            {"role": "user", "content": search_query}
        ]
        
        # Generate a response from OpenAI's GPT-3 model
        
        
        # Extract and display the articles and links from the OpenAI response
        conversation.append({"role":"user","content":" give the links out as complete links instead of clickable links format them into neat text"})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation
        )
        articles_and_links = response['choices'][0]['message']['content']
        links = re.findall(r'https?://[^\s]+', articles_and_links)
        x = articles_and_links
        link = re.findall(r'www?://[^\s]+', articles_and_links)
        lines = []

        for i in link:
            links.append[i]
        # Render the HTML template with search results directly
        return render_template('index.html', links = links, content = articles_and_links)
    
    except Exception as e:
        error_message = 'Error: ' + str(e)
        return render_template('error.html', error_message=error_message)

if __name__ == '__main__':
    app.run(port=8080, debug=True)
