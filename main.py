from dotenv import load_dotenv
import os
import requests

load_dotenv(".env")
API_BASE_URL = "https://newsapi.org/v2/everything?q=microsoft&sortBy=publishedAt&apiKey="
KEY = os.getenv("API_KEY")
REQUEST_URL = API_BASE_URL + KEY

req = requests.get(REQUEST_URL)
content = req.json()

for article in content["articles"]:
    print(article["title"])
    print(article["description"])


