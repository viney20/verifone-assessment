# app.py
from flask import Flask, request, jsonify
from jinja2 import Template
import json
app = Flask(__name__)

@app.route('/', methods=['GET'])
def respond():
    # Return the response in json format
    return jsonify({"Message": "Connection Success"}), 200

@app.route('/add', methods=['POST'])
def create_script():
    payload = json.loads(request.json)
    #tm = Template(templates.isolated_footer)
    #return tm.render(**payload)
    return json.dumps(payload)

@app.route('/listall', methods=['GET'])
def create_script():
    #payload = json.loads(request.json)
    #tm = Template(templates.isolated_footer)
    #return tm.render(**payload)
    return jsonify({"Message": "Connection Success"}), 200

@app.route('/<id>}', methods=['PUT'])
def create_script(id):
    #payload = json.loads(request.json)
    #tm = Template(templates.isolated_footer)
    #return tm.render(**payload)
    # Return the response in json format
    return jsonify({"Message": "Connection Success"}), 200

@app.route('/<id>', methods=['DELETE'])
def create_script(id):
    return json.dumps({'id':id}), 200

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000, debug=True)
