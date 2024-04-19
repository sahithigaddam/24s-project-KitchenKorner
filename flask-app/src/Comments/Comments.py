from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

comments = Blueprint('comments', __name__)

# Returns all comments under a post
@comments.route('/comments/<post_id>', methods=['GET'])
def get_comments(post_id):
    cursor = db.get_db().cursor()
    cursor.execute('select * from Comments where Post_ID = {0}'.format(post_id))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Turn off comments under a post
@comments.route('/comments/<post_id>', methods=['DELETE'])
def turn_off_comments(post_id):
    cursor = db.get_db().cursor()
    cursor.execute('DELETE FROM Comments WHERE id = {0}'.format(post_id))
    db.get_db().commit()
    return make_response(jsonify({"message": "Comments turned off successfully"}), 200)

# Specific user adding a comment to a post
@comments.route('/comments/<post_id>', methods=['POST'])
def add_comment(post_id):
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    text = the_data['Comment_Text']
    post_id = the_data['Post_ID']

    user_query = "SELECT User_ID FROM Users ORDER BY Created_At DESC LIMIT 1"
    current_app.logger.info(user_query)

    cursor = db.get_db().cursor()
    cursor.execute(user_query)
    user_result = cursor.fetchone()  # Fetch one row since we're expecting only one result
    user_id = user_result[0]  # Extract the user ID from the result

    # Constructing the query
    query = 'insert into Comments (Comment_Text, Post_ID, User_ID) values ("'
    query += text + '", "'
    query += str(post_id )+ '", "'
    query += str(user_id) + ')'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'

# Delete a comment under a post from a specific user
@comments.route('/comments/<comment_id>/<post_id>/<user_id>', methods=['DELETE'])
def delete_comment(comment_id, post_id, user_id):
    cursor = db.get_db().cursor()
    cursor.execute('DELETE FROM Comments WHERE Comment_ID = %s AND Post_ID = %s AND User_ID = %s', (Comment_ID, Post_ID, User_ID))
    db.get_db().commit()
    return make_response(jsonify({"message": "Comment deleted successfully"}), 200)
