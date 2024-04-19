from dotenv import load_dotenv
import os
import requests

load_dotenv(".env")
API_BASE_URL = "https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey="
KEY = os.getenv("API_KEY")
REQUEST_URL = API_BASE_URL + KEY

req = requests.get(REQUEST_URL)
content = req.text

print(content)