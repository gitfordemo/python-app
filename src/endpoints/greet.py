
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/greet', methods=['GET'])
def greet():
    return jsonify(message="Welcome to my Python project!")

@app.route('/api/greet', methods=['POST'])
def greet_post():
    data = request.get_json()
    name = data.get('name', 'Guest')
    return jsonify(message=f"Welcome to my Python project, {name}!")


if __name__ == "__main__":
    app.run(debug=True)