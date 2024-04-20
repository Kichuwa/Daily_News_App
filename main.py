from dotenv import load_dotenv
from modules.send_email import send_news_email
import os
import requests

load_dotenv(".env")
API_BASE_URL = "https://newsapi.org/v2/everything?q=microsoft&Language=en&sortBy=publishedAt&apiKey="
KEY = os.getenv("API_KEY")
REQUEST_URL = API_BASE_URL + KEY

req = requests.get(REQUEST_URL)
content = req.json()

news_titles = []
news_descriptions = []
news_url = []
article_count = 0

for article in content["articles"]:
    if article["title"] is not None:
        news_titles.append(article["title"])
        news_descriptions.append(article["description"])
        news_url.append(article["url"])
        article_count = article_count + 1

raw_message = ""
index = 0
while index < 10:
    raw_message += (str(news_titles[index]) + "\n" +
                    str(news_descriptions[index]) + "\n" +
                    str(news_url[index]) + 2*"\n")
    index = index + 1

# Remove raw message post testing
print(raw_message)

# the encode removes the issue that arrives from various ascii chars that may appear.
email_output = f"""\
Subject: Your Daily MS News!

{raw_message}

That was your TOP 10 recent news for the day!
""".encode('ascii', 'ignore')

send_news_email(email_output)
