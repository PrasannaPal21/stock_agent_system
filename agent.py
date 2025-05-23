# agent.py
# from adk import Agent
from identify_ticker import identify_ticker
from ticker_news import get_ticker_news
from ticker_price import get_ticker_price
from ticker_price_change import get_price_change
from ticker_analysis import analyze_ticker

def route_query(query: str) -> str:
    ticker = identify_ticker(query)
    if not ticker:
        return "Sorry, I couldn't identify the stock ticker from your query."

    query_lower = query.lower()

    if "news" in query_lower or "happening" in query_lower:
        news = get_ticker_news(ticker)
        if isinstance(news, str):
            return news
        return "\n".join([f"{i+1}. {article['title']}" for i, article in enumerate(news[:3])])

    elif "price change" in query_lower or "changed" in query_lower:
        return get_price_change(ticker, days=7)

    elif "drop" in query_lower or "increase" in query_lower or "analysis" in query_lower or "why" in query_lower:
        return analyze_ticker(ticker, days=7)

    elif "price" in query_lower or "current" in query_lower:
        return get_ticker_price(ticker)

    else:
        return "I understand you're asking about a stock, but could you clarify if you want the price, news, change, or analysis?"

class Agent:
    def __init__(self, name, description, instructions, route):
        self.name = name
        self.description = description
        self.instructions = instructions
        self.route = route
# Define the Google ADK Agent
agent = Agent(
    name="Stock Multi-Agent Analyst",
    description="I analyze stock data using news and market data from Alpha Vantage.",
    instructions="You can ask about stock prices, changes, news, or analysis.",
    route=route_query,
)

