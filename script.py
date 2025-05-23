import requests

response = requests.post(
    "http://127.0.0.1:5000/query",
    json={"query": "What is the latest news about Apple?"}
)
print(response.json())