import os
import ssl
import smtplib

def send_news_email(email_content):
    """
    Takes formatted string message from news API to send using hardcoded SMTP information from
    ENV file or Development/Path Environment variables
    :param email_content:
    :return:
    """
    host = os.getenv("HOST")
    port = os.getenv("PORT")

    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")

    receiver = os.getenv("RECEIVER")
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, email_content)
