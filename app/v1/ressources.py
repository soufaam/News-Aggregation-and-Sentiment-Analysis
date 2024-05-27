#!/usr/bin/env python
"""Ressources definition"""
from app.v1 import api
from endpoints import NewsScore

api.add_resource(NewsScore, '/news')
api.add_resource()