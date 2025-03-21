from keybert import KeyBERT

class Topics:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.kw_model = KeyBERT(model=model_name)

    def extract_topics(self, text, top_n=5):
        keywords = self.kw_model.extract_keywords(text, keyphrase_ngram_range=(1, 2), stop_words='english', top_n=top_n)
        return [kw[0] for kw in keywords]

    def compare_topics(self, news_data):
        article_topics = {f"Article {i+1}": self.extract_topics(article['summary']) for i, article in enumerate(news_data['articles'])}

        for i, article in enumerate(news_data['articles']):
            news_data['articles'][i]['Topics'] = list(article_topics.values())[i]

        all_topics = [topic for topics in article_topics.values() for topic in topics]
        common_topics = list(set([topic for topic in all_topics if all_topics.count(topic) > 1]))
        topic_overlap = {"Common Topics": common_topics}

        for article, topics in article_topics.items():
            topic_overlap[f'unique_topics in {article}'] = list(set(topics) - set(common_topics))

        news_data['Comparative Sentiment Score']['Topic Overlap'] = topic_overlap
        return news_data
