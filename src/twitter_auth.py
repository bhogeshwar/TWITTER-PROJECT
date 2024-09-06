# twitter_auth.py
import tweepy
from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, BEARER_TOKEN

def authenticate_twitter_app():
    # Set up Tweepy authentication for API v1.1 (for other v1.1 operations if needed)
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    # Set up Tweepy Client for API v2
    client = tweepy.Client(bearer_token=BEARER_TOKEN)

    # Verify credentials for v1.1 (optional, primarily for debugging)
    try:
        api.verify_credentials()
        print("Authentication OK")
    except Exception as e:
        print(f"Error during authentication: {e}")

    # Return the Client object, which is the one you need for v2 operations
    return client
