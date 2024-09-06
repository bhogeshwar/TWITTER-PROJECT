# collect_data.py
import tweepy
from twitter_auth import authenticate_twitter_app

# Define your query and number of tweets to fetch
query = '$spy -is:retweet lang:en'  # Refined query for better targeting; exclude retweets and specify language
count = 10  # Adjust this number according to the API's free-tier limits; usually max 10 or 100

# Authenticate and get the Client object for API v2 usage
client = authenticate_twitter_app()

try:
    # Fetch tweets using Twitter API v2 with the Client object
    response = client.search_recent_tweets(query=query, max_results=count, tweet_fields=['created_at', 'text'])

    if response.data:  # Check if response contains data
        tweets = response.data

        # Extract relevant tweet data
        tweet_data = [[tweet.created_at, tweet.text] for tweet in tweets]

        # Print fetched tweet data for verification
        for date, text in tweet_data:
            print(f"Date: {date}, Tweet: {text}")
    else:
        print("No tweets found for the given query.")

except tweepy.errors.TooManyRequests:
    print("Rate limit reached. Please try again later.")
except Exception as e:
    print(f"Error fetching tweets: {e}")



# def fetch_tweets(query, count=100):
#     api = authenticate_twitter_app()
#     tweets = tweepy.Cursor(api.search_tweets, q=query, lang="en", tweet_mode='extended').items(count)
#     tweet_data = [[tweet.created_at, tweet.full_text] for tweet in tweets]
#     return tweet_data
