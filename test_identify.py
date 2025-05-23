# test_identify.py
from identify_ticker import identify_ticker

queries = [
    "Why did Tesla stock drop today?",
    "What's happening with Palantir stock recently?",
    "How has Nvidia stock changed in the last 7 days?",
    "Tell me about Microsoft stock"
]

for q in queries:
    ticker = identify_ticker(q)
    print(f"Query: {q}\n → Ticker: {ticker}\n")
