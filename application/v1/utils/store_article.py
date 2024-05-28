#!/usr/bin/env python
"""store analysed article to db"""
from application.v1 import mongo


def store_articles_to_db(article):
    """_summary_
    """
    mongo.db.articles.insert_one(article)
