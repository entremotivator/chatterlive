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
        return "Invalid URL format. Please enter a valid URL."

# Text input for the URL with unique identifier
input_url = st.text_input("Enter the URL with the unique identifier:", key="input_url")

# Display the new URL if input is valid
if input_url:
    new_url = generate_new_url(input_url)
    if new_url.startswith("Invalid"):
        st.error(new_url)
    else:
        st.write("New URL:", new_url)
