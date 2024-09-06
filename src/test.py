# collect_data.py
import tweepy
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Fetch Bearer Token
BEARER_TOKEN = os.getenv('BEARER_TOKEN')

# Initialize the Client object with the Bearer Token for v2 endpoints
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# Define a simple query to fetch recent tweets
query = '$spy -is:retweet lang:en'  # Adjust query as needed

try:
    # Fetch tweets using API v2 endpoint with only the Bearer Token
    response = client.search_recent_tweets(query=query, max_results=10, tweet_fields=['created_at', 'text'])

    if response.data:
        for tweet in response.data:
            print(f"Date: {tweet.created_at}, Tweet: {tweet.text}")
    else:
        print("No tweets found for the given query.")

except tweepy.errors.Forbidden as e:
    print("403 Forbidden: Ensure your app is linked to a project and using the correct Bearer Token.")
except Exception as e:
    print(f"Error fetching tweets: {e}")
