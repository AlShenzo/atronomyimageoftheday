import requests
import streamlit as st
# get the url of the website and read as json
url = 'https://api.nasa.gov/planetary/apod?api_key=CCozDazv6dNPQIeM1GnAJfUkv5ldVIeBmhbRAc7v'

api_key='CCozDazv6dNPQIeM1GnAJfUkv5ldVIeBmhbRAc7v'

request = requests.get(url)

content = request.json()
# get the image that we want
url_image = content['url']

image = requests.get(url_image).content
# save it to the same directory
with open('image.jpg', 'wb') as file:
    picture = file.write(image)

# use st to create the page
st.header(content['title'])
st.text(content['date'])
st.image('image.jpg', caption=f'Image of {content['title']}')
# as the last sentence is unrelated in the dict
# split them and -1 the last sentece
# join them as strings
texts = content['explanation'].split('.')

final_text = texts[:-1]
paragraph = ' '.join(final_text)
print(content)
st.write(paragraph +'.', height=200)


