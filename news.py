import requests

# Replace 'YOUR_API_KEY' with your actual News API key
api_key = '4d28967db8624f0eb0eca67fbf492984'

# Specify the base URL for the News API
base_url = 'https://newsapi.org/v2/top-headlines?'

# Define the parameters for your news query
parameters = {
    'country': 'US',   # You can change the country code
    'apiKey': api_key
}

# Make a GET request to the News API
response = requests.get(base_url, params=parameters)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    news_data = response.json()

    # Check if articles are present in the response
    if 'articles' in news_data:
        # Iterate through the articles and print their titles
        for article in news_data['articles']:
            print(article['title'])
    else:
        print('No articles found in the response.')
else:
    print('Failed to retrieve news data. Status code:', response.status_code)
  
