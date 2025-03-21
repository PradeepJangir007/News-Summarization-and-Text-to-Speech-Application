from utils import NewsFetcher
from sentiment_analyzer import SentimentAnalyzer
from summarization import ArticleComparer
from Topic_Analysis import Topics

class NewsPipeline:
    """Class to handle the entire news processing pipeline."""
    def __init__(self, company_name):
        self.company_name = company_name
        self.news_data = None

    def fetch_news(self):
        """Fetches news articles for the given company."""
        news_fetcher = NewsFetcher()
        self.news_data = news_fetcher.fetch_news(self.company_name)
        del news_fetcher  # Free up memory

    def analyze_sentiment(self):
        """Performs sentiment analysis on fetched articles."""
        sentiment_analyzer = SentimentAnalyzer()
        self.news_data = sentiment_analyzer.analyze_sentiment(self.news_data)
        self.news_data = sentiment_analyzer.calculate_sentiment_distribution(self.news_data)
        del sentiment_analyzer  # Free up memory

    def analyze_topics(self):
        """Performs topic analysis on news articles."""
        topic_analyzer = Topics()
        self.news_data = topic_analyzer.compare_topics(self.news_data)
        del topic_analyzer  # Free up memory

    def compare_articles(self):
        """Compares articles and generates final summary."""
        article_comparer = ArticleComparer()
        self.news_data = article_comparer.compare_articles(self.news_data)
        self.news_data = article_comparer.get_final_summary(self.news_data)
        del article_comparer  # Free up memory



    def run_pipeline(self):
        """Executes the full news processing pipeline."""
        self.fetch_news()
        self.analyze_sentiment()
        self.analyze_topics()
        self.compare_articles()
        return self.news_data
