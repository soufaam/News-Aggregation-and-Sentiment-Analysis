#!/usr/bin/env python
"""_summary_"""
from newsapi import NewsApiClient
from dotenv import load_dotenv
import os


def fetch_everythings_news(subject=None):
    """fetch every news function"""
    load_dotenv()
    api = NewsApiClient(api_key=os.getenv('NEWS_API_KEY'))
    if subject:
            news = api.get_everything(q=subject, sort_by='popularity')
            articles = news.get('articles')
    else:
        news = api.get_everything(sort_by='popularity')
        articles = news.get('articles')
    return articles


def fetch_top_headlines(subject=None):
    """fetch every news function"""
    load_dotenv()
    api = NewsApiClient(api_key=os.getenv('NEWS_API_KEY'))
    top_headlines = api.get_everything(q=subject, sort_by='popularity')
    articles = top_headlines.get('articles')
    return articles
