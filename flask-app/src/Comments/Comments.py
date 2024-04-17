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

# Returns the comment of a specific user under a post
# @comments.route('/comments/<comment_id>/<post_id>/<user_id>', methods=['GET'])
# def get_specific_user_comment(comment_id, post_id, user_id):
#     cursor = db.get_db().cursor()
#     cursor.execute('SELECT * FROM Comments WHERE Comment_ID = %s AND Post_ID = %s AND User_ID = %s', (Comment_ID, Post_ID, User_ID))
#     row_headers = [x[0] for x in cursor.description]
#     json_data = []
#     theData = cursor.fetchall()
#     for row in theData:
#         json_data.append(dict(zip(row_headers, row)))
#     the_response = make_response(jsonify(json_data))
#     the_response.status_code = 200
#     the_response.mimetype = 'application/json'
#     return the_response

# Specific user adding a comment to a post
@comments.route('/comments/<post_id>/<user_id>', methods=['POST'])
def add_comment(post_id, user_id):
    comments_info = request.json
    current_app.logger.info(comments_info)
    text = comments_info['text']

    cursor = db.get_db().cursor()
    cursor.execute('INSERT INTO Comments (Post_ID, User_ID, Text) VALUES (%s, %s, %s)', (Post_ID, User_ID, Text))
    db.get_db().commit()
    return 'Succussfully added comment!'

# Delete a comment under a post from a specific user
@comments.route('/comments/<comment_id>/<post_id>/<user_id>', methods=['DELETE'])
def delete_comment(comment_id, post_id, user_id):
    cursor = db.get_db().cursor()
    cursor.execute('DELETE FROM Comments WHERE Comment_ID = %s AND Post_ID = %s AND User_ID = %s', (Comment_ID, Post_ID, User_ID))
    db.get_db().commit()
    return make_response(jsonify({"message": "Comment deleted successfully"}), 200)
