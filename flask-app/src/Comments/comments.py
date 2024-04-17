from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

comments = Blueprint('comments', __name__)

# Returns all comments under a post
@comments.route('/comments/<post_id>', methods=['GET'])
def get_comments(post_id):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM comments WHERE post_id = %s', (post_id,))
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
    cursor.execute('DELETE FROM comments WHERE post_id = %s', (post_id,))
    db.get_db().commit()
    return make_response(jsonify({"message": "Comments turned off successfully"}), 200)

# Returns the comment of a specific user under a post
@comments.route('/comments/<comment_id>/<post_id>/<user_id>', methods=['GET'])
def get_specific_user_comment(comment_id, post_id, user_id):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM comments WHERE comment_id = %s AND post_id = %s AND user_id = %s', (comment_id, post_id, user_id))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Specific user adding a comment to a post
@comments.route('/comments/<post_id>/<user_id>', methods=['POST'])
def add_comment(post_id, user_id):
    comments_info = request.json
    current_app.logger.info(comments_info)
    text = comments_info['text']

    cursor = db.get_db().cursor()
    cursor.execute('INSERT INTO comments (post_id, user_id, text) VALUES (%s, %s, %s)', (post_id, user_id, text))
    db.get_db().commit()
    return 'Succussfully added comment!'

# Delete a comment under a post from a specific user
@comments.route('/comments/<comment_id>/<post_id>/<user_id>', methods=['DELETE'])
def delete_comment(comment_id, post_id, user_id):
    cursor = db.get_db().cursor()
    cursor.execute('DELETE FROM comments WHERE comment_id = %s AND post_id = %s AND user_id = %s', (comment_id, post_id, user_id))
    db.get_db().commit()
    return make_response(jsonify({"message": "Comment deleted successfully"}), 200)
