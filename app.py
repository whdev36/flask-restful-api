from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def get_user():
    users = [
        {"id": 1, "name": "John Doe", "email": "john.doe@example.com"},
        {"id": 2, "name": "Jane Smith", "email": "jane.smith@example.com"}
    ]
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)