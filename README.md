# Stock Agents System

A multi-agent system for analyzing stock data using news and market data from Alpha Vantage and NewsAPI. The system can answer questions about stock prices, price changes, news, and provide simple analysis, either via a web interface or programmatically.

## Features
- Query latest stock news, price, and price changes
- Simple price and news-based analysis
- Web interface and API endpoint
- Easily extensible for more stocks or data sources

## Requirements
- Python 3.8+
- API keys for [Alpha Vantage](https://www.alphavantage.co/support/#api-key) and [NewsAPI](https://newsapi.org/register)

## Installation
1. Clone the repository and navigate to the project directory.
2. Create and activate a virtual environment:
   ```sh
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On Mac/Linux:
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```sh
   pip install flask requests python-dotenv
   ```
4. Create a `.env` file in the project root with your API keys:
   ```env
   ALPHA_VANTAGE_API_KEY=your_alpha_vantage_key
   NEWS_API_KEY=your_newsapi_key
   ```

## Usage

### Web Interface
1. Start the web server:
   ```sh
   python web_server.py
   ```
2. Open your browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
3. Enter your stock-related question in the form and view the response instantly.

### API Endpoint
- **POST** `/query` with JSON body:
  ```json
  { "query": "What is the latest news about Apple?" }
  ```
- Example using `curl`:
  ```sh
  curl -X POST http://127.0.0.1:5000/query -H "Content-Type: application/json" -d "{\"query\": \"What is the latest news about Apple?\"}"
  ```

### Script Usage
You can also use the system programmatically. Example (`script.py`):
```python
import requests
response = requests.post(
    "http://127.0.0.1:5000/query",
    json={"query": "What is the latest news about Apple?"}
)
print(response.json())
```

## Testing
Test scripts are provided for each module (e.g., `test_news.py`, `test_price.py`). Run them with:
```sh
python test_news.py
python test_price.py
python test_analysis.py
```

## Environment Variables
- `ALPHA_VANTAGE_API_KEY`: Your Alpha Vantage API key
- `NEWS_API_KEY`: Your NewsAPI key

## Project Structure
- `web_server.py` — Flask web server and web UI
- `agent.py` — Main agent logic and query routing
- `ticker_news.py`, `ticker_price.py`, `ticker_price_change.py`, `ticker_analysis.py` — Data fetching and analysis modules
- `identify_ticker.py` — Maps company names to stock tickers
- `test_*.py` — Test scripts for each module
- `script.py` — Example of programmatic API usage

## License
MIT (or specify your license)

## Sample Queries & Expected Outputs

| Query                                         | Example Output (shortened)                |
|-----------------------------------------------|-------------------------------------------|
| Why did Tesla stock drop today?               | 1. Tesla faces supply chain issues...<br>2. Market reacts to earnings report...<br>3. Analyst downgrades stock... |
| What's happening with Palantir stock recently?| 1. Palantir announces new government contract...<br>2. Stock surges after earnings...<br>3. CEO interview highlights growth... |
| How has Nvidia stock changed in the last 7 days?| From 2023-05-10 to 2023-05-17, the price changed from $280.00 to $295.00.<br>That's a change of 15.0 USD (5.36%). |
| What is the latest news about Apple?          | 1. Apple unveils new product lineup...<br>2. iPhone sales exceed expectations...<br>3. Apple invests in AI research... | 


##screenshots
![ss1](/ss1.jpg?raw=true)
![ss2](/ss2.jpg?raw=true)
![ss3](/ss3.jpg?raw=true)

