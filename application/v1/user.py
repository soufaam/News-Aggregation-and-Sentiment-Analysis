#!/usr/bin/env python
"""user class"""
from flask_restful import Resource
from flask import request
from application.v1 import bcrypt, mongo, jwt
from flask import jsonify
from flask_jwt_extended import (create_access_token,
                                get_jwt_identity, jwt_required, get_jwt)
from datetime import timedelta
import redis


class UserRegister(Resource):
    """Ressource Class"""

    def post(self):
        """POST request handling"""
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        if username:
            user = mongo.db.users.find_one({"username": username})
            if user:
                print(user)
                return {"error": 'Already exist'}, 400
            elif password:
                hashed_password = \
                    bcrypt.generate_password_hash(password=password)
                mongo.db.users.insert_one(
                    {'username': username, 'password': hashed_password})
                access_token = create_access_token(identity=username)
                return {"message": 'Register Success',
                        "access_token": access_token}, 200
            else:
                return {"error": "Missing password"}, 400
        else:
            return {"error": 'Missing username'}, 400


class UserLogin(Resource):
    def post(self):
        """GET request handling"""
        data = request.get_json()
        if data:
            username = data.get('username')
            password = data.get('password')
            if username:
                result_db = mongo.db.users.find_one({"username": username})
                if result_db:
                    pw_hash = result_db.get('password')
                    username = result_db.get('username')
                    if bcrypt.check_password_hash(pw_hash, password):
                        access_token = create_access_token(
                            identity=result_db.get('username'))
                        return {
                            "message": 'Login Success',
                            "access_token": access_token}, 200
                    else:
                        return {"message": 'Login Failed'}, 401
                else:
                    return {"message": 'Login Failed'}, 401
            else:
                return {"error": 'Missing username'}, 400
        return {"error": 'Missing username'}, 400


jwt_redis_block_list = redis.StrictRedis(
    host="localhost",
    port=6379, db=0,
    decode_responses=True
)


@jwt.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload: dict):
    jti = jwt_payload["jti"]
    token_in_redis = jwt_redis_block_list.get(jti)
    return token_in_redis is not None


class UserLogout(Resource):
    """User Logout
    Args:
        Resource (_type_): _description_
    """
    @jwt_required()
    def delete(self):
        """User logout """
        ACCESS_EXPIRES = timedelta(hours=1)
        jti = get_jwt()["jti"]
        jwt_redis_block_list.set(jti, "", ex=ACCESS_EXPIRES)
        return jsonify(message="Logout success")
