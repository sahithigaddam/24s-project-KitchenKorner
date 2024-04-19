from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

tags = Blueprint('tags', __name__)

# Returns all the users tagged in one post
@tags.route('/tags/<post_id>/<user_id>', methods=['GET'])
def get_tags(post_id, user_id):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Tags WHERE Post_ID = %s AND User_ID = %s', (post_id, user_id))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Add a tag to a post
@tags.route('/tags/<post_id>/<user_id>', methods=['POST'])
def tag_user():
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    post_id = the_data['Post_ID']
    user_id = the_data["User_id"]

    # Constructing the query
    query = 'insert into Tags (Post_ID, User_ID) values ("'
    query += post_id + '")'
    query += user_id + '")'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'