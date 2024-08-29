import requests
import os

from dotenv import load_dotenv

load_dotenv()

API_KEY=os.getenv('API_KEY')
url=os.getenv('URL')
#Make request to the API
request=requests.get(url)

#Get dictionary from the request
content=request.json()

#Access articles title and description
for article in content['articles']:
    print(article['title'])
    print(article['description'])