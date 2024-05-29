#!/usr/bin/env python
from flask_restful import Resource
from application.v1 import mongo
from flask import jsonify
from pprint import pprint
from bson import json_util
from flask import json, request
from application.v1.utils.fetch_news import on_demand_fetch_top_headlines
from application.v1.utils.fetch_and_process import fetch_and_analyse


class NewsScore(Resource):
    """_summary_NewsScore Class
    Args:
        Resource (_type_): _description_
    """
    def get(self):
        """get request handling"""
        articles = mongo.db.articles.find()
        articles_list = [article for article in articles]
        pprint(articles_list)
        return json.loads(json_util.dumps(articles_list))

    def post():
        """Post request handling """
        data = request.get_json()
        language = data.get('language')
        sources = data.get('sources')
        q = data.get('q')
        pageSize = data.get('pageSize')
        from_date = data.get('from')
        to_date = data.get('to')
        sortBy = data.get('sortBy')


class TopNewsScore(Resource):
    """
    TopHeadline class
    """
    def get():
        """get request handling"""

    def post():
        """Post request handling"""
        data = request.get_json()
        articles = on_demand_fetch_top_headlines(data)
        fetch_and_analyse(articles=articles)
