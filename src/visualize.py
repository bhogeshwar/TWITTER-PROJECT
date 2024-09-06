# visualize.py
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def visualize_sentiment(sentiment_data):
    df = pd.DataFrame(sentiment_data, columns=['Date', 'Tweet', 'Cleaned_Tweet', 'Sentiment'])
    sns.countplot(x='Sentiment', data=df)
    plt.title('Sentiment Analysis of Tweets')
    plt.xlabel('Sentiment')
    plt.ylabel('Number of Tweets')
    plt.show()
