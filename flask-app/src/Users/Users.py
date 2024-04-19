# Users 

from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

users = Blueprint('users', __name__)
# Get direct messages for a specific user
# @users.route('/users/<id>', methods=['GET'])
# def get_user_recipes(id):  
    
#     user_query = "SELECT User_ID FROM Users ORDER BY Created_At DESC LIMIT 1"
#     current_app.logger.info(user_query)

#     cursor = db.get_db().cursor()
#     cursor.execute(user_query)
#     user_result = cursor.fetchone()  # Fetch one row since we're expecting only one result
#     id = user_result[0]  # Extract the user ID from the result

#     query = 'SELECT User_ID FROM Users WHERE User_ID = ' + str(id)
#     current_app.logger.info(query)

#     cursor = db.get_db().cursor()
#     cursor.execute(query)
#     column_headers = [x[0] for x in cursor.description]
#     json_data = []
#     the_data = cursor.fetchall()
#     for row in the_data:
#         json_data.append(dict(zip(column_headers, row)))
#     return jsonify(json_data)

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

# # Get the user's own posts
# @users.route('/users/<user_id>', methods=['GET'])
# def get_user_posts(user_id):

#     user_query = "SELECT User_ID FROM Users ORDER BY Created_At DESC LIMIT 1"
#     current_app.logger.info(user_query)

#     cursor = db.get_db().cursor()
#     cursor.execute(user_query)
#     user_result = cursor.fetchone()  # Fetch one row since we're expecting only one result
#     user_id = user_result[0]  # Extract the user ID from the result

#     query = 'SELECT Posts.Post_ID, Username, Recipe_Name, Recipe_Image, Meal_Type,\
#         Cuisine, Expected_Time, Expected_Difficulty FROM Users JOIN Feeds ON Feeds.User_ID = Users.User_ID\
#         JOIN Follows ON Feeds.User_ID = Follows.Follower_ID\
#         JOIN Posts ON Posts.User_ID = Follows.Followee_ID JOIN Recipes ON Recipes.Post_ID = Posts.Post_ID WHERE Feeds.User_ID = ' + str(user_id)
#     current_app.logger.info(query)

#     cursor = db.get_db().cursor()
#     cursor.execute(query)
#     column_headers = [x[0] for x in cursor.description]
#     json_data = []
#     the_data = cursor.fetchall()
#     for row in the_data:
#         json_data.append(dict(zip(column_headers, row)))
#     return jsonify(json_data)

# Get user's info
@users.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    
    user_query = "SELECT User_ID FROM Users ORDER BY Created_At DESC LIMIT 1"
    current_app.logger.info(user_query)

    cursor = db.get_db().cursor()
    cursor.execute(user_query)
    user_result = cursor.fetchone()  # Fetch one row since we're expecting only one result
    user_id = user_result[0]  # Extract the user ID from the result

    query = "SELECT * FROM Users WHERE User_ID = " + str(user_id)
    current_app.logger.info(query)
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    the_data = cursor.fetchall()
    for row in the_data:
        json_data.append(dict(zip(column_headers, row)))
    return jsonify(json_data)

# Get user's info
@users.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    
    user_info = request.json
    username = user_info['Username']
    full_name = user_info['Full_Name']
    email = user_info['Email']

    user_query = "SELECT User_ID FROM Users ORDER BY Created_At DESC LIMIT 1"
    current_app.logger.info(user_query)

    cursor = db.get_db().cursor()
    cursor.execute(user_query)
    user_result = cursor.fetchone()  # Fetch one row since we're expecting only one result
    user_id = user_result[0]  # Extract the user ID from the result

    query = "UPDATE Users SET Username = %s, Full_Name = %s, Email = %s where User_ID = %s"
    data = (username, full_name, email, user_id)
    cursor = db.get_db().cursor()
    cursor.execute(query, data)
    db.get_db().commit()
    return 'User updated!'

# Delete a user from the paltform
@users.route('/users', methods=['DELETE'])
def delete_user(user_id):
    cursor = db.get_db().cursor()
    query = "DELETE FROM Users WHERE User_ID = %s"
    cursor.execute(query, (user_id,))
    db.get_db().commit()
    return make_response(jsonify({"message": "User deleted successfully"}), 200)
