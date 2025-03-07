import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
import logging

# Configure logging
logging.basicConfig(filename="sentiment.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def analyze_sentiment(text):
    """Analyze sentiment of a given text."""
    polarity = TextBlob(text).sentiment.polarity
    sentiment = "positive" if polarity > 0 else "negative" if polarity < 0 else "neutral"
    logging.info(f"Text: {text} | Sentiment: {sentiment} | Score: {polarity}")
    return sentiment

def read_reviews(file_path="reviews.txt"):
    """Read reviews from a file if it exists."""
    return open(file_path, encoding="utf-8").read().splitlines() if os.path.exists(file_path) else []

def main():
    print("🔹 Sentiment Analysis Tool 🔹\nEnter text or type 'exit' to stop.")

    reviews = read_reviews()
    user_reviews = []
    
    while (review := input("\nEnter a review: ")) != "exit":
        user_reviews.append(review)
    
    all_reviews = reviews + user_reviews
    df = pd.DataFrame({"Review": all_reviews, "Sentiment": [analyze_sentiment(r) for r in all_reviews]})
    
    print("\n📊 Sentiment Analysis Results:\n", df)
    
    plt.figure(figsize=(6, 4))
    sns.countplot(data=df, x="Sentiment", palette="coolwarm")
    plt.title("Sentiment Distribution")
    plt.show()

if __name__ == "__main__":
    main()
