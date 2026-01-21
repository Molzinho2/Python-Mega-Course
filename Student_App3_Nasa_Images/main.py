import streamlit as st
import requests

api_key = "YOUR API TOKEN"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
response = requests.get(url)
data = response.json()

title = data['title']
date = data['date']
img_raw = data['url']
description = data['explanation']

img_loc = requests.get(img_raw)

with open('image.jpg','wb') as file:
    file.write(img_loc.content)

st.title(title)
st.write(date)
st.image('image.jpg')
st.write(description)

