# Users 

from flask import Blueprint, request, jsonify, make_response
import json
from src import db

users = Blueprint('users', __name__)

# Return a list of all usernames for search
@users.route('/users', methods=['GET'])
def get_users():
    cursor = db.get_db().cursor()
    cursor.execute('select User_ID, Username, Email, Full_Name, Created_At from users')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Add a new user who joins the platform
@users.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    cursor = db.get_db().cursor()
    query = "INSERT INTO users (User_ID, Username, Email, Full_Name, Created_At) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (data['User_ID'], data['Username'], data['Email'], data['Full_Name'], data['Created_At']))
    db.get_db().commit()
    return make_response(jsonify({"message": "User added successfully"}), 201)

# Delete a user from the paltform
@users.route('/users', methods=['DELETE'])
def delete_user(user_id):
    cursor = db.get_db().cursor()
    query = "DELETE FROM customers WHERE id = %s"
    cursor.execute(query, (user_id,))
    db.get_db().commit()
    return make_response(jsonify({"message": "User deleted successfully"}), 200)