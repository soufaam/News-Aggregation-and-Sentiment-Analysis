#!/usr/bin/env python
"""Create Flask App"""
from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_pymongo import PyMongo
from flask_apscheduler import APScheduler
from dotenv import load_dotenv
import os
from flask_bcrypt import Bcrypt
from datetime import timedelta


load_dotenv()
ACCESS_EXPIRES = timedelta(hours=1)
app = Flask(__name__)
api = Api(app)
app.config['JWT_SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = ACCESS_EXPIRES
app.config['MONGO_URI'] = 'mongodb://localhost:27017/news_db'
jwt = JWTManager(app)
mongo = PyMongo(app)
bcrypt = Bcrypt(app)
scheduler = APScheduler()
scheduler.api_enabled = True
scheduler.init_app(app=app)
