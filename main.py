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

# Function to fetch news articles
def fetch_news():
    response = requests.get(base_url, params=parameters)
    if response.status_code == 200:
        return response.json().get('articles', [])
    else:
        st.write('Failed to retrieve news data. Status code:', response.status_code)
        return []

# Initialize the list of articles
articles = fetch_news()
current_article_index = 0

# Display the app title
st.title("News Headlines")

# Check if articles are present
if articles:
    # Create buttons for navigation
    next_button = st.button("Next")
    prev_button = st.button("Previous")

    if next_button:
        # Show the next article
        current_article_index = (current_article_index + 1) % len(articles)

    if prev_button:
        # Show the previous article
        current_article_index = (current_article_index - 1) % len(articles)

    # Display the current article's title
    st.write(articles[current_article_index]['title'])
else:
    st.write('No articles found.')
