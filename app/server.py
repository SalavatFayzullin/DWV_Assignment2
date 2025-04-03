from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
packages = []

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json
    packages.append(data)
    return jsonify({"status": "success"})

@app.route('/get_data')
def get_data():
    return jsonify(packages)

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)