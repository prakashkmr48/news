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

# Define custom CSS for styling headlines with horizontal scrolling and changing colors
custom_css = """
<style>
.news-container {
    width: 100%;
    overflow: hidden;
}

.news-headline {
    white-space: nowrap;
    font-size: 24px;
    font-weight: bold;
    padding: 10px 20px; /* Expand padding to cover the entire news */
    margin-right: 20px; /* Add space between headlines */
    background-color: #f0f0f0;
    border-radius: 5px;
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);
    animation: scrollText 10s linear infinite, changeColor 10s linear infinite;
}

@keyframes scrollText {
    0% {
        transform: translateX(100%);
    }
    100% {
        transform: translateX(-100%);
    }
}

@keyframes changeColor {
    0%, 100% {
        background-color: #f0f0f0;
    }
    50% {
        background-color: #ffa500; /* Change color when news changes */
    }
}
</style>
"""

# Display the app title
st.title("News Headlines")

# Inject custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Create a button to show API Documentation
if st.button("API Documentation"):
    # Display the entire API documentation when the button is clicked
    st.markdown("""
    # News Headlines API Documentation

    ## Introduction

    The News Headlines API provides access to a Streamlit app that displays news headlines from various sources. The API is designed to showcase news headlines in a visually appealing way, with horizontal scrolling and changing colors. This documentation outlines how to use the API to retrieve and display news headlines.

    **Base URL:** https://newsapi.org/v2/top-headlines?

    ## Endpoints

    ### Get News Headlines

    - **Endpoint:** `/get_headlines`
    - **Method:** GET
    - **Description:** Retrieve a list of news headlines.
    - **Parameters:**
      - `country` (optional): Specify the country code to filter news headlines by country. Default is 'US'.
      - `pageSize` (optional): Set the number of articles per page. Default is 10.
    - **Response:**
      - Status Code: 200 OK
      - Content-Type: text/html
      - Body: HTML containing news headlines

    ## Usage

    To retrieve news headlines, make a GET request to the `/get_headlines` endpoint. You can specify optional query parameters to filter and customize the results.

    ### Example Request

    ```
    GET /get_headlines?country=US&pageSize=10
    ```

    ### Example Response

    ```html
    <!DOCTYPE html>
    <html>
    <head>
        <!-- CSS and JavaScript resources are included here -->
    </head>
    <body>
        <div class="news-container">
            <div class="news-headline">Headline 1</div>
            <div class="news-headline">Headline 2</div>
            <!-- Additional headlines go here -->
        </div>
    </body>
    </html>
    ```

    ## CSS Customization

    The API includes custom CSS for styling the news headlines. You can adjust the CSS styles to modify the appearance of the headlines, including fonts, colors, and animations. Refer to the HTML `<style>` block in the response for details.

    ## Pagination

    The API currently displays news headlines as a continuous loop with horizontal scrolling. You can pause and resume the headlines using the "Pause News" checkbox on the webpage.

    ## Rate Limiting

    The News Headlines API does not impose rate limits, as it is intended for demonstration purposes. However, consider implementing rate limiting in your own applications to prevent excessive requests.

    ## Error Handling

    - If the API encounters an error while retrieving news data from the source, it will respond with an error message and an appropriate HTTP status code.

    ## Disclaimer

    This API is provided for demonstration purposes and may not provide real-time or up-to-date news headlines. The use of the News API for production purposes may require integration with a real news data source.

    ## Contact

    If you have any questions or need assistance, please contact prakashkmr48@gmail.com.

  """)
else:
    # Check if headlines are present
    if all_headlines:
        # Create a container for displaying headlines with horizontal scrolling
        st.markdown('<div class="news-container">', unsafe_allow_html=True)

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
                # Apply custom CSS to the headline
                headline_html = f'<div class="news-headline">{all_headlines[current_headline_index]}</div>'
                headline_placeholder.markdown(headline_html, unsafe_allow_html=True)

                # Update the index for the next headline
                current_headline_index = (current_headline_index + 1) % len(all_headlines)

            # Sleep for 10 seconds before displaying the next headline (slower scrolling)
            time.sleep(10)
    else:
        st.write('No headlines found.')
