from flask import Blueprint, request, jsonify, make_response
import json
from src import db

tags = Blueprint('tags', __name__)

# Returns all the users tagged in one post
@tags.route('/tags/<post_id>/<user_id>', methods=['GET'])
def get_tags(post_id, user_id):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM tags WHERE post_id = %s AND user_id = %s', (post_id, user_id))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response