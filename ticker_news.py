# ticker_news.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_ticker_news(ticker: str, limit=5):
    api_key = os.getenv("NEWS_API_KEY")
    url = f"https://newsapi.org/v2/everything?q={ticker}&sortBy=publishedAt&pageSize={limit}&apiKey={api_key}"
    
    response = requests.get(url)
    if response.status_code != 200:
        return f"Error fetching news: {response.status_code}"

    articles = response.json().get("articles", [])
    if not articles:
        return f"No news found for {ticker}."

    news_items = []
    for article in articles:
        news_items.append({
            "title": article["title"],
            "url": article["url"],
            "published": article["publishedAt"]
        })

    return news_items
