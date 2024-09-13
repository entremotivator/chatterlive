import streamlit as st

# Base URL
base_url = "https://desktop.chattersocial.io/rooms/"

# Function to modify /room/ to /rooms/ and generate new URL
def generate_new_url(input_url):
    if "/room/" in input_url:
        # Replace /room/ with /rooms/
        new_url = input_url.replace("/room/", "/rooms/")
        return new_url
    return None

# App title
st.title("URL Generator")

# Instructions
st.write("Enter the URL with the unique identifier to generate the new URL:")

# Text input for the URL with unique identifier
input_url = st.text_input("URL with Unique Identifier", placeholder="https://www.chattersocial.io/room/db2b9be8-ea26-471c-8f60-06aa7a8bf7e1")

# Button to generate the new URL
if st.button("Enter"):
    new_url = generate_new_url(input_url)
    if new_url:
        st.success("New URL Generated:")
        st.write(new_url)
    else:
        st.error("Invalid URL format. Please enter a valid URL.")
