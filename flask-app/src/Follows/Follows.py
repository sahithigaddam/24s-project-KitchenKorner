# Follows

from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

follows = Blueprint('follows', __name__)

# Get followers for particular user
@follows.route('/follows/<followee_id>', methods=['GET'])
def get_followers(followee_id):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Follows WHERE Followee_ID = {0}'.format(followee_id))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@follows.route('/follows/followee_id', methods=['POST'])
def follow_user(followee_id):
    # Query to get the follower ID
    follower_query = "SELECT User_ID FROM Users ORDER BY Created_At DESC LIMIT 1"
    current_app.logger.info(follower_query)

    cursor = db.get_db().cursor()
    cursor.execute(follower_query)
    follower_result = cursor.fetchone() # Fetch one row since we're expecting only one result
    id = follower_result[0] # Extract the follower ID from the result
    
    the_data = request.json
    current_app.logger.info(the_data)

    query = 'insert into follows (Followee_ID, Follower_ID) values (%s, %s)"'

    cursor.execute(query, (followee_id, id))
    db.get_db().commit()
      
    return 'Success!'

# Unfollow a user
@follows.route('/unfollows/<followee_id>', methods=['DELETE'])
def remove_follower(followee_id):
    # Query to get the follower ID
    follower_query = "SELECT User_ID FROM Users ORDER BY Created_At DESC LIMIT 1"
    current_app.logger.info(follower_query)

    cursor = db.get_db().cursor()
    cursor.execute(follower_query)
    follower_result = cursor.fetchone() # Fetch one row since we're expecting only one result
    id = follower_result[0] # Extract the follower ID from the result

    data = request.get_json()
    cursor = db.get_db().cursor()
    query = "DELETE FROM Follows WHERE Followee_ID = %s AND Follower_ID = %s"
    cursor.execute(query, (followee_id, id))
    db.get_db().commit()
    return make_response(jsonify({"message": "Successfully unfollowed user"}), 200)