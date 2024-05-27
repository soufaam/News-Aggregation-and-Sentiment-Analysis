#!/usr/bin/env python
from flask_restful import Resource


class NewsScore(Resource):
    """_summary_NewsScore Class

    Args:
        Resource (_type_): _description_
    """
    def get(self):
        """get request handling"""
        return