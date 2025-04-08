# tests/test_sentiment.py
from app.sentiment import analyze_sentiment

def test_analyze_sentiment_positive():
    polarity, sentiment = analyze_sentiment("I love this post!")
    assert sentiment == "positive"
    assert polarity > 0

def test_analyze_sentiment_negative():
    polarity, sentiment = analyze_sentiment("This is terrible.")
    assert sentiment == "negative"
    assert polarity < 0