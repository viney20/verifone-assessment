# app.py
from flask import Flask, request, jsonify
from jinja2 import Template
import json
app = Flask(__name__)
MOBILE_ENTRIES ={}
def create_data(simcard, mobile_no,  status, expire , state, kyc, provider, full_name):
    payload = {
        "simcard": simcard,
        "mobile_no":mobile_no,
        "status": status,
        "expire": expire,
        "state" :state,
        "kyc":kyc,
        "provider":provider,
        "full_name":full_name,
    }



@app.route('/', methods=['GET'])
def respond():
    # Return the response in json format
    return jsonify({"Message": "Connection Success"}), 200

@app.route('/add', methods=['POST'])
def add_entry():
    payload = request.json
    params = ["Sim_card_no","Mobile_no", "Status","State_of_registration", "Expiry_date","KYC","Telecom_Provider","Full_name"]
    for param in params:
        if(param not in payload):
            return jsonify({'error': f'parameter {param}  missing in payload'}), 400 

    entry = create_data(*[payload[param] for param in params])
    global MOBILE_ENTRIES
    MOBILE_ENTRIES[payload["Sim_card_no"]]= entry
    return jsonify({"Message": "Entry Successful"}), 200

@app.route('/listall', methods=['GET'])
def list_entry():
    return jsonify(MOBILE_ENTRIES), 200

@app.route('/<id>}', methods=['PUT'])
def edit_entry(id):
    #payload = json.loads(request.json)
    #tm = Template(templates.isolated_footer)
    #return tm.render(**payload)
    # Return the response in json format
    return jsonify({"Message": "Connection Success"}), 200

@app.route('/<id>', methods=['DELETE'])
def delete_entry(id):
    return json.dumps({'id':id}), 200

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000, debug=True)
