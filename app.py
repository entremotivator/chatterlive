import streamlit as st

# Base URL
base_url = "https://dev-web.chattersocial.io/rooms/"

# Input URL
input_url = st.text_input("Enter the URL with the unique identifier:", "https://www.chattersocial.io/rooms/db2b9be8-ea26-471c-8f60-06aa7a8bf7e1")

if input_url:
    # Extract the unique identifier from the input URL
    try:
        unique_id = input_url.split("/rooms/")[1]
        # Combine the base URL with the unique identifier
        new_url = base_url + unique_id

        # Display the new URL
        st.write("New URL:", new_url)
    except IndexError:
        st.error("Invalid URL format. Please enter a valid URL.")
