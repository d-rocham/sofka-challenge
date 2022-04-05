""" Create api blueprint, initialize Flaks_restful's api object and add the api resources """

from flask import Blueprint, Flask
from flask_restful import Api

from .resources import questions

api_bp = Blueprint("api", __name__)
api = Api(api_bp, errors=Flask.errorhandler, catch_all_404s=True)


api.add_resource(questions, "/api/questions/", endpoint="questions")
