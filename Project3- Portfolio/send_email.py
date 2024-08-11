import smtplib,ssl
from dotenv import load_dotenv
import os

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    # Load environment variables from .env file
    load_dotenv()

    # Access environment variables
    username = os.getenv('GMAIL_USERNAME')
    password = os.getenv('GMAIL_PASSWORD')
    receiver=os.getenv('receiver')
    
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver,message)
