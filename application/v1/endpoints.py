#!/usr/bin/env python
from flask_restful import Resource
from application.v1 import mongo
from flask import jsonify
from pprint import pprint
from bson import json_util
from flask import json, request
from application.v1.utils.fetch_news import (on_demand_fetch_top_headlines,
                                             on_demand_fetch_every_news)
from application.v1.utils.fetch_and_process import fetch_and_analyse
from flask_jwt_extended import jwt_required, get_jwt_identity


class NewsScore(Resource):
    """_summary_NewsScore Class
    Args:
        Resource (_type_): _description_
    """
    @jwt_required()
    def get(self):
        """get request handling"""
        articles = mongo.db.articles.find()
        articles_list = [article for article in articles]
        pprint(articles_list)
        return json.loads(json_util.dumps(articles_list))

    @jwt_required()
    def post(self):
        """Post request handling """
        data = request.get_json()
        articles = on_demand_fetch_every_news(**data)
        if articles == []:
            return {"error": 'newsApi error: Invalid  parameter'}, 401
        articles = fetch_and_analyse(articles=articles)
        return json.loads(json_util.dumps(articles))


class TopNewsScore(Resource):
    """
    TopHeadline class
    """
    @jwt_required()
    def get(self):
        """get request handling"""

    @jwt_required()
    def post(self):
        """Post request handling"""
        current_user = get_jwt_identity()
        data = request.get_json()
        articles = on_demand_fetch_top_headlines(**data)
        if articles == []:
            return {"error": 'newsApi error: Invalid  parameter'}, 401
        articles = fetch_and_analyse(articles=articles)
        return json.loads(json_util.dumps(articles))
