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

# Function to fetch all news articles and store them in a list
def fetch_and_store_all_news():
    all_articles = []
    current_page = 1
    while True:
        parameters['page'] = current_page
        response = requests.get(base_url, params=parameters)
        if response.status_code == 200:
            news_data = response.json()
            articles = news_data.get('articles', [])
            if not articles:
                break
            all_articles.extend(articles)
            current_page += 1
        else:
            st.write('Failed to retrieve news data. Status code:', response.status_code)
            break
    return all_articles

# Fetch all news articles and store them
all_news = fetch_and_store_all_news()
current_article_index = 0

# Display the app title
st.title("News Headlines")

# Check if articles are present
if all_news:
    # Create buttons for navigation
    next_button = st.button("Next")
    prev_button = st.button("Previous")

    if next_button:
        # Show the next article
        current_article_index = (current_article_index + 1) % len(all_news)

    if prev_button:
        # Show the previous article
        current_article_index = (current_article_index - 1) % len(all_news)

    # Display the current article's title
    st.write(all_news[current_article_index]['title'])
else:
    st.write('No articles found.')
