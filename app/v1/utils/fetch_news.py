#!/usr/bin/env python
"""_summary_"""
from newsapi import NewsApiClient
from dotenv import load_dotenv
import os

def fetch_everythings_news(subject):
    """fetch every news function"""
    load_dotenv()
    api = NewsApiClient(api_key=os.getenv('SECRET_KEY'))
    news = api.get_everything(q=subject, sort_by='popularity')
    articles = news.get('articles')
    return articles


def fetch_top_headlines(subject=None):
    """fetch every news function"""
    load_dotenv()
    api = NewsApiClient(api_key=os.getenv('SECRET_KEY'))
    top_headlines = api.get_everything(q=subject, sort_by='popularity')
    articles = top_headlines.get('articles')
    return articles
