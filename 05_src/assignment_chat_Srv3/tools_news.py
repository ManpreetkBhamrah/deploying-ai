from langchain.tools import tool
import json
import requests
import os
@tool
def get_latest_news(n: int = 1):
    """Returns n latestnews headlines."""
    apiKey = os.getenv('NEWS_API')
    url = "https://newsapi.org/v2/top-headlines" 
    params = { "sources": "bbc-news",
               "apiKey": apiKey } 
    response = requests.get(url, params=params) 
        
    if response.status_code == 200:
        data = response.json()
        articles = data.get("articles", [])[:n]
        headlines = [article["title"] for article in articles]
        return headlines
    else:
        return f"Error fetching news: {response.status_code}"
