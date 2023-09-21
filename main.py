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

    # Create a "Stop" button
    stop_button = st.button("Stop")

    # Automatically update headlines in a continuous loop
    while run_headlines:
        # Display the current headline
        headline_placeholder.write(all_headlines[current_headline_index])

        # Update the index for the next headline
        current_headline_index = (current_headline_index + 1) % len(all_headlines)

        # Sleep for 3 seconds before displaying the next headline
        time.sleep(3)

        # Check if the "Stop" button is clicked
        if stop_button:
            run_headlines = False  # Stop the loop when the button is clicked

    # Display a message when the loop is stopped
    st.write("Loop stopped.")
else:
    st.write('No headlines found.')
