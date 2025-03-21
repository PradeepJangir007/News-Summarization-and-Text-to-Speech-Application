import requests
from bs4 import BeautifulSoup

class NewsFetcher:
    """Class to fetch relevant news articles for a given company from Times of India."""
    def __init__(self):
        self.base_url = "https://timesofindia.indiatimes.com/topic/"
        self.headers = {"User-Agent": "Mozilla/5.0"}
        self.news_data ={'Company':None}

    def fetch_news(self, company):
        self.news_data['Company']=company
        """Fetches news articles related to the given company.""" #Fixed: Removed extra indentation before docstring.
        url = f"{self.base_url}{company.replace(' ', '-')}"  # Convert spaces to dashes for URL compatibility
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching news: {e}")
            return []

        try:
            soup = BeautifulSoup(response.text, "html.parser")
        except Exception as e:
            print(f"Error parsing webpage: {e}")
            return []

        articles = []
        try:
            news_items = soup.find_all("div", class_="uwU81")  # Selecting relevant news containers

            for item in news_items:
                try:
                    title = item.find('span').get_text() if item.find('span') else "No Title"
                    summary = item.find('p').get_text() if item.find('p') else "No Summary"

                    # Convert to lowercase for better matching
                    if company.lower() in title.lower() or company.lower() in summary.lower():
                        articles.append({
                            "title": title,
                            "summary": summary,
                        })
                except Exception as e:
                    print(f"Error processing a news item: {e}")
                    continue  # Skip this item and continue with the next one
        except Exception as e:
            print(f"Error extracting news items: {e}")
            return []
        self.news_data['articles']= articles if articles else [{"message": "No relevant articles found"}]
        return self.news_data
