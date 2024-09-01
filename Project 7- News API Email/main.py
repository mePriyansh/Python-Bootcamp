import requests
import os
from send_email import send_email
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set the topic for the news search
topic = "tesla"

# Get the API key from environment variables
API_KEY = os.getenv('API_KEY')

# Construct the URL for the API request
url = f"https://newsapi.org/v2/everything?q={topic}&from=2024-08-10&sortBy=publishedAt&apiKey={API_KEY}&language=en"

# Make the request to the API
request = requests.get(url)

# Get the dictionary from the request
content = request.json()

# Access articles title and description
body = ""
for article in content['articles'][:20]:
    if article["title"] is not None:
        description = article["description"] if article["description"] is not None else "No description available"
        body = "Subject: Today's News" + "\n" + body + article["title"] + "\n" + description + "\n" + article["url"] + "\n\n"

# Convert body to UTF-8 to avoid encoding issues
body = body.encode("utf-8")

# Send the email using the send_email function
send_email(message=body)
