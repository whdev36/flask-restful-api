from flask import request
from flask_restful import Resource

# Simple resource
class HelloWorld(Resource):
    def get(self):
        return {'message': 'Hello World!'}
