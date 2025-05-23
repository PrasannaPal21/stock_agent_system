# test_news.py
from ticker_news import get_ticker_news

ticker = "TSLA"
news = get_ticker_news(ticker)

print(f"Recent news for {ticker}:")
for item in news:
    print(f"- {item['title']} ({item['published']})\n  {item['url']}\n")
