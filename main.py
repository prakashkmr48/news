import streamlit as st
import requests

# Replace 'YOUR_API_KEY' with your actual News API key
api_key = '4d28967db8624f0eb0eca67fbf492984'

# Specify the base URL for the News API
base_url = 'https://newsapi.org/v2/top-headlines?'

# Define the parameters for your news query
country = 'US'   # You can change the country code
page_size = 5    # Number of articles per page
parameters = {
    'country': country,
    'apiKey': api_key,
    'pageSize': page_size
}

# Function to fetch news articles
def fetch_news(page):
    parameters['page'] = page
    response = requests.get(base_url, params=parameters)
    if response.status_code == 200:
        return response.json().get('articles', [])
    else:
        st.write('Failed to retrieve news data. Status code:', response.status_code)
        return []

# Initialize variables
current_page = 1
articles = fetch_news(current_page)
current_article_index = 0

# Display the app title
st.title("News Headlines")

# Check if articles are present
if articles:
    # Create buttons for navigation
    next_button = st.button("Next")
    prev_button = st.button("Previous")

    if next_button:
        current_article_index = 0  # Reset to the first article on a new page
        current_page += 1
        articles = fetch_news(current_page)

    if prev_button:
        current_article_index = 0  # Reset to the first article on a new page
        current_page = max(1, current_page - 1)
        articles = fetch_news(current_page)

    # Display the current article's title
    st.write(articles[current_article_index]['title'])
else:
    st.write('No articles found.')
