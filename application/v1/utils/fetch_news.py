#!/usr/bin/env python
"""_summary_"""
from newsapi import NewsApiClient
from dotenv import load_dotenv
import os
from pprint import pprint


def default_fetch_everythings_news():
    """fetch every news function"""
    load_dotenv()
    api = NewsApiClient(api_key=os.getenv('NEWS_API_KEY'))
    news = api.get_everything(sort_by='popularity')
    articles = news.get('articles')
    return articles


def default_fetch_top_headlines():
    """fetch every news function"""
    load_dotenv()
    api = NewsApiClient(api_key=os.getenv('NEWS_API_KEY'))
    articles = []
    top_headlines_ma = api.get_top_headlines(country='ma')
    top_headlines_us = api.get_top_headlines(country='us')
    top_headlines_fr = api.get_top_headlines(country='fr')
    top_headlines_sa = api.get_top_headlines(country='sa')
    articles_ma = top_headlines_ma.get('articles')
    articles_fr = top_headlines_fr.get('articles')
    articles_us = top_headlines_us.get('articles')
    articles_sa = top_headlines_sa.get('articles')
    if articles_ma:
        articles.extend(articles_ma)
    if articles_us:
        articles.extend(articles_us)
    if articles_fr:
        articles.extend(articles_fr)
    if articles_sa:
        articles.extend(articles_sa)
    return articles


def on_demand_fetch_top_headlines(**kwargs):
    """On demand fetch top headlines"""
    language = kwargs.get('language')
    sources = kwargs.get('sources')
    q = kwargs.get('q')
    page_size = kwargs.get('pageSize')
    category = kwargs.get('category')
    country = kwargs.get('country')
    load_dotenv()
    try:
        api = NewsApiClient(api_key=os.getenv('NEWS_API_KEY1'))
        on_demand_top_head = api.get_top_headlines(
            q=q, language=language,
            country=country,
            sources=sources, page_size=page_size,
            category=category)
    except ValueError:
        return []
    articles = on_demand_top_head.get('articles')
    return articles


def on_demand_fetch_every_news(**kwargs):
    """Search through millions of articles from
    over 150,000 large and small news sources and blogs.
    """
    language = kwargs.get('language')
    sources = kwargs.get('sources')
    q = kwargs.get('q')
    page_size = kwargs.get('pageSize')
    category = kwargs.get('category')
    sort_by = kwargs.get('sort_by')
    domains = kwargs.get('domains')
    to_param = kwargs.get('to_param')
    from_param = kwargs.get('from_param')
    load_dotenv()
    api = NewsApiClient(api_key=os.getenv('NEWS_API_KEY'))
    on_demand_top_head = api.get_everything(q=q, language=language,
                                            sources=sources,
                                            page_size=page_size,
                                            domains=domains,
                                            sort_by=sort_by,
                                            category=category,
                                            to=to_param,
                                            from_param=from_param)
    articles = on_demand_top_head.get('articles')
    return articles
