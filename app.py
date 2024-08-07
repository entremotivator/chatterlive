import streamlit as st

# Base URL
base_url = "https://dev-web.chattersocial.io/rooms/"

# Function to extract unique identifier and generate new URL
def generate_new_url(input_url):
    try:
        unique_id = input_url.split("/rooms/")[1]
        new_url = base_url + unique_id
        return new_url
    except IndexError:
        return None

# App title
st.title("URL Generator")

# Instructions
st.write("Enter the URL with the unique identifier to generate the new URL:")

# Text input for the URL with unique identifier
input_url = st.text_input("URL with Unique Identifier", placeholder="https://www.chattersocial.io/rooms/db2b9be8-ea26-471c-8f60-06aa7a8bf7e1")

# Button to generate the new URL
if st.button("Enter"):
    new_url = generate_new_url(input_url)
    if new_url:
        st.success("New URL Generated:")
        st.write(new_url)
    else:
        st.error("Invalid URL format. Please
