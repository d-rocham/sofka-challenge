from flask_restful import Resource, reqparse


class questions(Resource):
    def get(self):
        parser = reqparse.RequestParser()
