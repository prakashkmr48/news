import streamlit as st
import requests
import time

# Replace 'YOUR_API_KEY' with your actual News API key
api_key = '4d28967db8624f0eb0eca67fbf492984'

# Specify the base URL for the News API
base_url = 'https://newsapi.org/v2/top-headlines?'

# Define the parameters for your news query
parameters = {
    'country': 'US',   # You can change the country code
    'apiKey': api_key,
    'pageSize': 10  # Adjust the number of articles per page as needed
}

# Function to fetch headlines
def fetch_headlines():
    response = requests.get(base_url, params=parameters)
    if response.status_code == 200:
        news_data = response.json()
        headlines = [article['title'] for article in news_data.get('articles', [])]
        return headlines
    else:
        st.write('Failed to retrieve news data. Status code:', response.status_code)
        return []

# Fetch and store headlines
all_headlines = fetch_headlines()

# Display the app title
st.title("News Headlines")

# Check if headlines are present
if all_headlines:
    # Create a placeholder for displaying headlines
    headline_placeholder = st.empty()

    # Create a boolean variable to control the loop
    run_headlines = True

    # Initialize the current headline index
    current_headline_index = 0

    # Create a "Display News" button
    display_button = st.button("Display News")

    # Create a "Resume News" button
    resume_button = st.button("Resume News")

    # Automatically update headlines in a continuous loop
    while run_headlines:
        # Check if the "Display News" button is clicked
        if display_button:
            headline_placeholder.write(all_headlines[current_headline_index])
            display_button = False  # Reset the button state

        # Update the index for the next headline
        current_headline_index = (current_headline_index + 1) % len(all_headlines)

        # Sleep for 3 seconds before displaying the next headline
        time.sleep(3)

        # Check if the "Resume News" button is clicked
        if resume_button:
            resume_button = False  # Reset the button state

    # Display a message when the loop is paused
    st.write("News paused.")
else:
    st.write('No headlines found.')
