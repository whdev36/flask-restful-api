from flask import request
from flask_restful import Resource

# Simple resource
class HelloWorld(Resource):
    def get(self):
        return {'message': 'Hello World!'}

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

class Person(Resource):
    def get(self, name):
        if name in persons:
            person = persons[name]
            return  person, 200
        else:
            return {'error': 'Person not found.'}