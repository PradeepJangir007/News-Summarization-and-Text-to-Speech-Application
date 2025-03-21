from transformers import pipeline

class SentimentAnalyzer:
    def __init__(self):
        self.pipeline = pipeline("sentiment-analysis", model="mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis")

    def analyze_sentiment(self, news_data):
        for article in news_data['articles']:
            text = article["title"] + ". " + article["summary"]
            sentiment = self.pipeline(text)[0]
            article["sentiment"] = sentiment['label']
        return news_data
    def calculate_sentiment_distribution(self,news_data):
        """Calculates sentiment distribution from the given news articles data."""
        sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}

        for article in news_data['articles']:
            sentiment = article.get("sentiment", "").capitalize()
            if sentiment in sentiment_counts:
                sentiment_counts[sentiment] += 1

        news_data["Comparative Sentiment Score"]={"Sentiment Distribution": sentiment_counts}
        return news_data
