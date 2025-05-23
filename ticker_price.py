# ticker_price.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_ticker_price(ticker: str):
    api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey={api_key}"
    
    response = requests.get(url)
    if response.status_code != 200:
        return f"Error fetching price: {response.status_code}"

    data = response.json().get("Global Quote", {})
    if not data or "05. price" not in data:
        return f"No price data found for {ticker}."

    return {
        "ticker": ticker,
        "price": float(data["05. price"]),
        "change": data["09. change"],
        "percent_change": data["10. change percent"]
    }
