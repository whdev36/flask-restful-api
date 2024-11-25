from flask import Flask
from flask_restful import Api
from flask_cors import CORS
import resources as r # "r" is "resources"

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(r.HelloWorld, '/hw') # "hw" is "helloworld"
api.add_resource(r.Hello, '/hello/<string:name>') # This is Hello resource
api.add_resource(r.Student, '/student/<string:name>/<string:surname>/<int:age>/<int:id>') # This is Student resource
api.add_resource(r.Persons, '/persons') # Persons resource

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')