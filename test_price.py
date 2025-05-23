# test_price.py
from ticker_price import get_ticker_price

ticker = "TSLA"
price_info = get_ticker_price(ticker)

print(f"Price info for {ticker}:")
print(price_info)
