"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# Get all Family Members
@app.route('/members', methods=['GET'])
def handle_hello():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    if members:
        response_body = {
            "hello": "world",
            "family": members
        }
        return jsonify(response_body), 200
    else:
        return jsonify({"error": "No family members found"}),404

# 2 Retrieve one member
@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    if member:
        return jsonify(member), 200
    else:
        return jsonify({"error": "Member not found"}), 404


#3 Add (POST) new member
@app.route('/member', methods=['POST'])
def add_member():
    # List of required fields
    required_keys = {"first_name", "age", "Lucky Numbers"}
    
    # Get the incoming request body
    request_body = request.get_json(force=True)
    
    # Get the keys sent in the request
    request_keys = set(request_body.keys())
    
    # Check which required fields are missing
    missing_fields = required_keys - request_keys
    if missing_fields:
        return jsonify({"error": f"Missing required fields: {', '.join(missing_fields)}"}), 400

    # Only keep the required fields in the request
    filtered_member = {key: request_body[key] for key in required_keys if key in request_body}

    # Generate ID and create the member
    member = {
        "id": jackson_family._generateId(),
        **filtered_member  # Add only the filtered (required) fields
    }
    
    # Add the member
    jackson_family.add_member(member)
    return jsonify(member), 201




#def add_new_todo():
    # request_body = request.get_json(force=True)
    # print("Incoming request with the following body", request_body)
    # todos.append(request_body)
    # return jsonify(todos)


#4 DELETE one member

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
