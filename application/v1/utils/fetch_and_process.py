#!/usr/bin/env python
"""Fetch and process module"""
from .fetch_news import fetch_everythings_news, fetch_top_headlines
from .store_article import store_articles_to_db
from .sentiment_api import analyze_sentiment
from pprint import pprint


def fetch_and_analyse():
    """Fetch_and_analyse"""
    articles = fetch_top_headlines(subject='Ukraine')
    pprint(articles)
    for article in articles:
        sentiment = analyze_sentiment(article.get('description'))
        article['sentiment_score'] = sentiment.score
        article['sentiment_magnitude'] = sentiment.score
        store_articles_to_db(article=article)
