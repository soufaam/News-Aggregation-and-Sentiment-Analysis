#!/usr/bin/env python
"""Fetch and process module"""
from .fetch_news import (default_fetch_everythings_news,
                         default_fetch_top_headlines)
from .store_article import store_articles_to_db
from .sentiment_api import analyze_sentiment
from pprint import pprint


def default_fetch_and_analyse():
    """Fetch_and_analyse"""
    articles = default_fetch_top_headlines()
    for article in articles:
        description = article.get('description')
        if (description):
            sentiment = analyze_sentiment(description)
            article['sentiment_score'] = sentiment.score
            article['sentiment_magnitude'] = sentiment.score
            store_articles_to_db(article=article)


def fetch_and_analyse(articles):
    """Fetch_and_analyse"""
    articles_list = []
    article_dic = {}
    for article in articles:
        description = article.get('description')
        if (description):
            article_dic = article
            sentiment = analyze_sentiment(description)
            article_dic['sentiment_score'] = sentiment.score
            article_dic['sentiment_magnitude'] = sentiment.score
            store_articles_to_db(article=article_dic)
            articles_list.append(article_dic)
    return articles_list
