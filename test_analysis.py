# test_analysis.py
from ticker_analysis import analyze_ticker

ticker = "TSLA"
report = analyze_ticker(ticker, days=7)
print(report)
