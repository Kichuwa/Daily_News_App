from dotenv import load_dotenv
import os
import requests
import smtplib
import ssl

def send_news_email(email_content):
    host = os.getenv("HOST")
    port = os.getenv("PORT")

    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")

    receiver = os.getenv("RECEIVER")
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, email_content)


load_dotenv(".env")
API_BASE_URL = "https://newsapi.org/v2/everything?q=microsoft&Language=en&sortBy=publishedAt&apiKey="
KEY = os.getenv("API_KEY")
REQUEST_URL = API_BASE_URL + KEY

req = requests.get(REQUEST_URL)
content = req.json()

news_titles = []
news_descriptions = []
article_count = 0

for article in content["articles"]:
    news_titles.append(article["title"])
    news_descriptions.append(article["description"])
    article_count = article_count + 1

raw_message = ""
index = 0
while index < 10:
    raw_message += str(news_titles[index]) + "\n" + str(news_descriptions[index]) + "\n\n"
    index = index + 1

print(raw_message)

email_output = f"""\
Subject: Your Daily MS News!

{raw_message}

That was your TOP 10 recent news for the day!
""".encode('ascii', 'ignore')

send_news_email(email_output)
