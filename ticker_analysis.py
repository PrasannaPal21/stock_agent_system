# ticker_analysis.py
from ticker_price_change import get_price_change
from ticker_news import get_ticker_news

def analyze_ticker(ticker: str, days: int = 7):
    price_info = get_price_change(ticker, days)
    if isinstance(price_info, str):  # error message
        return price_info

    news = get_ticker_news(ticker)
    if isinstance(news, str):  # error message
        return news

    # Build summary
    summary = f"📈 **{ticker} Price Analysis (Last {days} Days)**\n"
    summary += f"From {price_info['from_date']} to {price_info['to_date']}, the price changed from ${price_info['start_price']} to ${price_info['end_price']}.\n"
    summary += f"That's a change of {price_info['change']} USD ({price_info['percent_change']}).\n\n"
    summary += "📰 **Recent News Headlines:**\n"

    for i, article in enumerate(news[:3], 1):
        summary += f"{i}. {article['title']}\n"

    return summary
