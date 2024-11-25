from flask_restful import Resource

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