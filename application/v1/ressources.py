#!/usr/bin/env python
"""Ressources definition"""
from application.v1 import api
from application.v1.endpoints import NewsScore
from application.v1.endpoints import TopNewsScore

api.add_resource(NewsScore, '/news')
api.add_resource(TopNewsScore, '/topnews')
