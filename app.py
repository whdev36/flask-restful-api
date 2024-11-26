from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/users', methods=['GET'])
def get_user():
    users = [
        {"id": 1, "name": "John Doe", "email": "john.doe@example.com"},
        {"id": 2, "name": "Jane Smith", "email": "jane.smith@example.com"}
    ]
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)