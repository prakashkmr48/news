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

# Define custom CSS for styling headlines
custom_css = """
<style>
.news-headline {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 10px;
    padding: 10px;
    background-color: #f0f0f0;
    border-radius: 5px;
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);
    animation: fadeInUp 0.5s ease-in-out;
}

@keyframes fadeInUp {
    0% {
        opacity: 0;
        transform: translateY(20px);
    }
    100% {
        opacity: 1;
        transform: translateY(0);
    }
}
</style>
"""

# Display the app title
st.title("News Headlines")

# Inject custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Check if headlines are present
if all_headlines:
    # Create a placeholder for displaying headlines
    headline_placeholder = st.empty()

    # Create a checkbox to pause and resume news
    pause_news = st.checkbox("Pause/Resume News")

    # Initialize the current headline index
    current_headline_index = 0

    # Automatically update headlines in a continuous loop
    while True:
        # Display the current headline if the "Pause/Resume News" checkbox is not selected
        if not pause_news:
            # Apply custom CSS to the headline
            headline_html = f'<div class="news-headline">{all_headlines[current_headline_index]}</div>'
            headline_placeholder.markdown(headline_html, unsafe_allow_html=True)

            # Update the index for the next headline
            current_headline_index = (current_headline_index + 1) % len(all_headlines)

        # Sleep for 3 seconds before displaying the next headline
        time.sleep(3)
else:
    st.write('No headlines found.')
