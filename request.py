import requests
import openai
import dotenv
import os
dotenv.load_dotenv()
key = os.getenv('CHATGPTKEY')

client = openai.OpenAI()
client.api_key = key

