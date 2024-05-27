#!/usr/bin/env python
"""store analysed article to db"""
from app.v1 import mongo


def store_articles_to_db(articles):
    """_summary_
    """
    mongo.db.articles.insert_many(articles)
