# ticker_price_change.py
import os
import requests
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()

def get_price_change(ticker: str, days: int = 7):
    api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={ticker}&apikey={api_key}"
    
    response = requests.get(url)
    if response.status_code != 200:
        return f"Error fetching time series: {response.status_code}"
    
    data = response.json().get("Time Series (Daily)", {})
    if not data:
        return f"No time series data found for {ticker}."

    # Sort dates to get most recent and past data
    dates = sorted(data.keys(), reverse=True)
    if len(dates) < days + 1:
        return f"Not enough data to calculate change over {days} days."

    try:
        latest_date = dates[0]
        past_date = dates[days]  # skip weekends/holidays: just use Nth previous day available

        latest_close = float(data[latest_date]["4. close"])
        past_close = float(data[past_date]["4. close"])
        change = latest_close - past_close
        percent_change = (change / past_close) * 100

        return {
            "ticker": ticker,
            "from_date": past_date,
            "to_date": latest_date,
            "start_price": round(past_close, 2),
            "end_price": round(latest_close, 2),
            "change": round(change, 2),
            "percent_change": f"{round(percent_change, 2)}%"
        }
    except Exception as e:
        return f"Error processing data: {str(e)}"
