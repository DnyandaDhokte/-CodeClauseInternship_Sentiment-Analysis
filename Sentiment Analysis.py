import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
import tkinter as tk
from tkinter import messagebox, scrolledtext
from collections import Counter
from io import BytesIO
from PIL import Image, ImageTk

# Function to analyze sentiment
def analyze_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    return "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"

# Function to update sentiment analysis
def update_analysis():
    review = entry.get("1.0", tk.END).strip()
    if not review:
        messagebox.showwarning("Warning", "Please enter a review!")
        return
    
    sentiment = analyze_sentiment(review)
    reviews.append((review, sentiment))
    text_display.insert(tk.END, f"Review: {review}\nSentiment: {sentiment}\n\n")
    entry.delete("1.0", tk.END)
    plot_sentiment()

# Function to plot sentiment distribution
def plot_sentiment():
    sentiments = [s for _, s in reviews]
    sentiment_counts = Counter(sentiments)
    df = pd.DataFrame(sentiment_counts.items(), columns=["Sentiment", "Count"])
    
    plt.figure(figsize=(4, 3), dpi=100)
    sns.barplot(x=df["Sentiment"], y=df["Count"], palette=["#ff4d6d", "#ff99a8", "#ffffff"])
    plt.title("Sentiment Distribution")
    plt.xticks(rotation=45)
    
    buf = BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)
    img = Image.open(buf)
    img = img.resize((300, 200), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    plot_label.config(image=img)
    plot_label.image = img
    plt.close()

# Initialize Tkinter window
root = tk.Tk()
root.title("Sentiment Analysis Tool")
root.geometry("500x600")
root.configure(bg="#ffccd5")

# UI Elements
title = tk.Label(root, text="🔹 Sentiment Analysis 🔹", font=("Arial", 16, "bold"), bg="#ffccd5", fg="#ff4d6d")
title.pack(pady=10)

entry = scrolledtext.ScrolledText(root, width=50, height=5, font=("Arial", 12))
entry.pack(pady=10)

analyze_button = tk.Button(root, text="Analyze Sentiment", command=update_analysis, font=("Arial", 12), bg="#ff4d6d", fg="white")
analyze_button.pack(pady=5)

text_display = scrolledtext.ScrolledText(root, width=50, height=10, font=("Arial", 12))
text_display.pack(pady=10)

plot_label = tk.Label(root, bg="#ffccd5")
plot_label.pack()

reviews = []

# Run application
root.mainloop()
