import requests
import os
from send_email import send_email

from dotenv import load_dotenv

load_dotenv()

API_KEY=os.getenv('API_KEY')
url=os.getenv('URL')
#Make request to the API
request=requests.get(url)

#Get dictionary from the request
content=request.json()

#Access articles title and description
body=""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + "\n\n"
    
body = body.encode("utf-8")    
send_email(message=body)