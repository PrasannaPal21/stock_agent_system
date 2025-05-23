# identify_ticker.py

TICKER_MAP = {
    "tesla": "TSLA",
    "apple": "AAPL",
    "amazon": "AMZN",
    "microsoft": "MSFT",
    "palantir": "PLTR",
    "nvidia": "NVDA",
    "google": "GOOGL",
    "meta": "META",
    "facebook": "META",
    "alphabet": "GOOGL",
}

def identify_ticker(query: str) -> str:
    query = query.lower()
    for name, ticker in TICKER_MAP.items():
        if name in query:
            return ticker
    return None
