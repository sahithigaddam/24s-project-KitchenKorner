# Users 

from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

users = Blueprint('users', __name__)

# Return a list of all usernames for search
@users.route('/users', methods=['GET'])
def get_users():
    cursor = db.get_db().cursor()
    cursor.execute('select User_ID, Username, Email, Full_Name, Created_At from Users')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    the_data = cursor.fetchall()
    for row in the_data:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Add a new user who joins the platform
@users.route('/users', methods=['POST'])
def add_new_user():
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    username = the_data['Username']
    email = the_data['Email']
    full_name = the_data['Full_Name']

    # Constructing the query
    query = 'insert into Users (Username, Email, Full_Name) values ("'
    query += username + '", "'
    query += email + '", "'
    query += full_name + '")'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'

# Delete a user from the paltform
@users.route('/users', methods=['DELETE'])
def delete_user(user_id):
    cursor = db.get_db().cursor()
    query = "DELETE FROM Users WHERE User_ID = %s"
    cursor.execute(query, (user_id,))
    db.get_db().commit()
    return make_response(jsonify({"message": "User deleted successfully"}), 200)
