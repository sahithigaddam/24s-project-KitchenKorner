from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

search = Blueprint('Search', __name__)

# Return a list of all usernames for search
@search.route('/Search/<username>', methods=['GET'])
def get_user_search_details(username):

    query = 'SELECT Username, Full_Name FROM Users WHERE Username LIKE %' + username
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    the_data = cursor.fetchall()
    for row in the_data:
        json_data.append(dict(zip(column_headers, row)))
    return jsonify(json_data)


# Add a new user search
@search.route('/Search', methods=['POST'])
def search_new_user():
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    username = the_data['Username']
    user_id = the_data['User_ID']

    # Constructing the query
    query = 'insert into Search (Username, User_ID) values ("'
    query += username + '", "'
    query += user_id + ')'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'


