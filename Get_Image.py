"""
This program extracts images and information from NASA's Astronomy Picture of the Day (APOD) API
and displays them using the Streamlit library on a local webhost.
"""
# Import the requests library for making HTTP requests
# Import the Streamlit library for creating web apps
import requests as rq
import streamlit as st

api_key = "GZfC0If6ua9XQIFanZw2xkbCDnCQqVF8ayArRarW"

# Construct the API URL with the API key
url = "https://api.nasa.gov/planetary/apod?&" \
      f"api_key={api_key}"

# Send a GET request to the API and get the response
response = rq.get(url)

# Convert the response to JSON format
data = response.json()

# Assign variables from the API response
title = data['title']              # Title of the image
explanation = data['explanation']  # Explanation of the image
image_url = data['url']            # URL of the image

# Set the file path to save the image
image_path = "image_jpg"

# Send a GET request to the image URL and get the image content
image = rq.get(image_url)

# Open the file in binary write mode and write the image content
with open(image_path, "wb") as file:
    file.write(image.content)

# Create a Streamlit app
st.title(title)                     # Display the title of the image
st.image(image_path)                # Display the image
st.write(explanation)               # Display the explanation of the image