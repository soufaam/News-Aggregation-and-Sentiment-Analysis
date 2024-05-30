#!/usr/bin/env python
"""Ressources definition"""
from application.v1 import api
from application.v1.endpoints import NewsScore
from application.v1.endpoints import TopNewsScore
from application.v1.user import UserLogin, UserRegister, UserLogout


api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')
api.add_resource(UserRegister, '/register')
api.add_resource(NewsScore, '/news')
api.add_resource(TopNewsScore, '/topnews')
