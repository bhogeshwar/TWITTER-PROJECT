# config.py
"""
Description:
-------------
This configuration file reads Twitter API credentials from environment variables.
The credentials are used for authenticating with the Twitter API via Tweepy.

Important:
-----------
Ensure environment variables are set up correctly before running the project.
"""

import os

# Read Twitter API credentials from environment variables
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')