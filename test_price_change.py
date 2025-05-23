# test_price_change.py
from ticker_price_change import get_price_change

ticker = "TSLA"
change_info = get_price_change(ticker, days=7)

print(f"Price change over 7 days for {ticker}:")
print(change_info)
