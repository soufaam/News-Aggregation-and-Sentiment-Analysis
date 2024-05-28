#!/usr/bin/env python
from flask_restful import Resource
from application.v1 import mongo
from flask import jsonify
from pprint import pprint
from bson import json_util
from flask import json


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
