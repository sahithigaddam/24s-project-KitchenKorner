from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

posts = Blueprint('posts', __name__)

# Create a post with a recipe
@posts.route('/posts/<post_id>/<recipe_id>', methods=['POST'])
def create_post(post_id, recipe_id):
    post_info = request.json
    current_app.logger.info(post_info)
    post_id = post_info['Post_ID']
    user_id = post_info['User_ID']
    filter_id = post_info['Filter_ID']
    created_at = post_info['Created_At']
    
    cursor = db.get_db().cursor()
    cursor.execute('INSERT INTO posts (post_id, recipe_id) VALUES (%s, %s)', (post_id, recipe_id))
    db.get_db().commit()
    return 'Successfully created a post!'

# Mark a post as archived
@posts.route('/posts/<post_id>', methods=['DELETE'])
def archive_post(post_id):
    cursor = db.get_db().cursor()
    cursor.execute('UPDATE posts SET archived = true WHERE post_id = %s', (post_id,))
    db.get_db().commit()
    return make_response(jsonify({"message": "Post archived successfully"}), 200)