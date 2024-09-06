# main.py
from collect_data import fetch_tweets
from preprocess import clean_text
from sentiment_analysis import get_sentiment
from visualize import visualize_sentiment

if __name__ == "__main__":
    # Fetch tweets related to a specific query
    query = "#YourTopic -filter:retweets"  # Replace #YourTopic with your desired topic
    tweets = fetch_tweets(query, count=100)

    # Clean and analyze tweets
    cleaned_tweets = [(date, tweet, clean_text(tweet)) for date, tweet in tweets]
    sentiment_data = [(date, tweet, cleaned, get_sentiment(cleaned)) for date, tweet, cleaned in cleaned_tweets]

    # Visualize sentiment distribution
    visualize_sentiment(sentiment_data)
