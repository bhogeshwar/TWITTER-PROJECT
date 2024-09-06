# config.py
"""
Description:
-------------
This configuration file reads Twitter API credentials from a .env file using python-dotenv.
Ensure that the .env file is properly set up in your project directory.

Important:
-----------
Keep the .env file secure and do not share it publicly.
"""

# config.py
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()  # This line should come before accessing environment variables

# Access Twitter API credentials
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
BEARER_TOKEN=os.getenv('BEARER_TOKEN')


# Debugging: Print loaded values to ensure they are being read correctly
print("Consumer Key:", CONSUMER_KEY)
print("Consumer Secret:", CONSUMER_SECRET)
print("Access Token:", ACCESS_TOKEN)
print("Access Token Secret:", ACCESS_TOKEN_SECRET)
print("BEARER_TOKEN:", BEARER_TOKEN)
