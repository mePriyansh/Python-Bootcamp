import streamlit as st
import requests
from dotenv import load_dotenv
import os

load_dotenv()
api= os.getenv('NASA_API_KEY')
url=f"https://api.nasa.gov/planetary/apod?api_key={api}"


response1 = requests.get(url)
content = response1.json()

title = content['title']
image_url = content['url']
body = content['explanation']

image_filepath = "img.png"
response2 = requests.get(image_url)
with open(image_filepath, 'wb') as file:
    file.write(response2.content)

st.title(title)
st.image(image_filepath)
st.write(body)