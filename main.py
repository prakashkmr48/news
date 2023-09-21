import streamlit as st
import requests

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
current_headline_index = 0

# Display the app title
st.title("News Headlines")

# Check if headlines are present
if all_headlines:
    # Create buttons for navigation
    next_button = st.button("Next")
    prev_button = st.button("Previous")

    if next_button:
        # Show the next headline
        current_headline_index = (current_headline_index + 1) % len(all_headlines)

    if prev_button:
        # Show the previous headline
        current_headline_index = (current_headline_index - 1) % len(all_headlines)

    # Display the current headline
    st.write(all_headlines[current_headline_index])

    # Add a button to fetch the full article for the current headline
    if st.button("Read Full Article"):
        article_url = [article['url'] for article in news_data.get('articles', [])][current_headline_index]
        st.markdown(f"Read the full article [here]({article_url}).")
else:
    st.write('No headlines found.')
