
# app/sentiment.py
from textblob import TextBlob

def analyze_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    classification = "positive" if polarity >= 0 else "negative"
    return polarity, classification