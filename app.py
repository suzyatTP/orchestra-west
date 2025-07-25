from flask import Flask, render_template, request, jsonify
import os
import json

app = Flask(__name__)
ASSIGNMENTS_FILE = 'assignments.json'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save():
    data = request.get_json()
    with open(ASSIGNMENTS_FILE, 'w') as f:
        json.dump(data, f)
    return jsonify(status="success")

@app.route('/load', methods=['GET'])
def load():
    if os.path.exists(ASSIGNMENTS_FILE):
        with open(ASSIGNMENTS_FILE, 'r') as f:
            return jsonify(json.load(f))
    return jsonify({})

if __name__ == '__main__':
    app.run(debug=True)
