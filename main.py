import streamlit as st
import requests
import time

# Replace 'YOUR_API_KEY' with your actual News API key
api_key = '4d28967db8624f0eb0eca67fbf492984'

# Define the base URL for the News API
base_url = 'https://newsapi.org/v2/top-headlines?'

# Function to fetch headlines based on the selected country
def fetch_headlines(country_code):
    parameters = {
        'country': country_code,
        'apiKey': api_key,
        'pageSize': 10  # Adjust the number of articles per page as needed
    }
    response = requests.get(base_url, params=parameters)
    if response.status_code == 200:
        news_data = response.json()
        headlines = [article['title'] for article in news_data.get('articles', [])]
        return headlines
    else:
        st.write('Failed to retrieve news data. Status code:', response.status_code)
        return []

# Display the app title
st.title("News Headlines")

# Create a dropdown menu for selecting the country
selected_country = st.selectbox("Select a country", ["US", "UK", "Canada", "Australia", "India"]) # Add more countries as needed

# Fetch and store headlines based on the selected country
all_headlines = fetch_headlines(selected_country)

# Check if headlines are present
if all_headlines:
    # Create a placeholder for displaying headlines
    headline_placeholder = st.empty()

    # Create a checkbox to pause and resume news
    pause_news = st.checkbox("Pause News")

    # Initialize the current headline index
    current_headline_index = 0

    # Automatically update headlines in a continuous loop
    while True:
        # Display the current headline if the "Pause News" checkbox is not selected
        if not pause_news:
            headline_placeholder.write(all_headlines[current_headline_index])

            # Update the index for the next headline
            current_headline_index = (current_headline_index + 1) % len(all_headlines)

        # Sleep for 3 seconds before displaying the next headline
        time.sleep(3)
else:
    st.write('No headlines found.')
