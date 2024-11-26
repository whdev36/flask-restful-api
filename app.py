from flask import Flask, jsonify
from flask_cors import CORS
from flask_restful import Api
import resources as r

app = Flask(__name__)
api = Api(app)
CORS(app)

@app.route('/users', methods=['GET'])
def get_user():
    users = [
        {"id": 1, "name": "John Doe", "email": "john.doe@example.com"},
        {"id": 2, "name": "Jane Smith", "email": "jane.smith@example.com"}
    ]
    return jsonify(users)

# Add resource to endpoint
api.add_resource(r.HelloWorld, '/')
api.add_resource(r.Person, '/person/<string:name>')

if __name__ == '__main__':
    app.run(debug=True)