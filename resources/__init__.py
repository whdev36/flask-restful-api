from flask_restful import Resource, reqparse
from flask import request, jsonify

class HelloWorld(Resource):
    def get(self):
        return {'message': 'Hello World!'}
    
    def post(self):
        return {'message': 'Posted successfully!'}

class Hello(Resource):
    def get(self, name):
        return {'message': f'Hello {name.title()}!'}

class Student(Resource):
    def get(self, name, surname, age, id):
        return {'name': name, 'surname': surname, 'age': age, 'id': id}

persons = { 
    'tim': {'age': 19, 'gender': 'male', 'job': 'student', 'city': 'New York'},
    'sarah': {'age': 22, 'gender': 'female', 'job': 'designer', 'city': 'San Francisco'},
    'john': {'age': 25, 'gender': 'male', 'job': 'developer', 'city': 'Seattle'},
    'lisa': {'age': 21, 'gender': 'female', 'job': 'nurse', 'city': 'Chicago'},
    'mike': {'age': 18, 'gender': 'male', 'job': 'intern', 'city': 'Austin'},
    'anna': {'age': 24, 'gender': 'female', 'job': 'teacher', 'city': 'Boston'},
    'james': {'age': 23, 'gender': 'male', 'job': 'engineer', 'city': 'Denver'},
    'emma': {'age': 20, 'gender': 'female', 'job': 'photographer', 'city': 'Los Angeles'},
    'noah': {'age': 26, 'gender': 'male', 'job': 'lawyer', 'city': 'Houston'},
    'olivia': {'age': 27, 'gender': 'female', 'job': 'chef', 'city': 'Miami'},
}

class Persons(Resource):
    def get(self):
        return persons

animes = {
    1: {"title": "Naruto", "genre": "Action", "episodes": 220},
    2: {"title": "Attack on Titan", "genre": "Adventure", "episodes": 75},
    3: {"title": "One Piece", "genre": "Adventure", "episodes": 1000},
}

class Anime(Resource):
    def get(self, id):
        if id not in animes:
            return {'error': 'Anime not found.'}, 404
        return jsonify(animes[id])
    def put(self, id):
        # Get JSON data
        return {}