from flask import Blueprint, request, jsonify, make_response
import json
from src import db

ratings = Blueprint('ratings', __name__)

# Returns all ratings under a post
@ratings.route('/ratings/<int:post_id>', methods=['GET'])
def get_ratings(post_id):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM ratings WHERE post_id = %s', (post_id,))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Update average taste rating of a post
@ratings.route('/ratings/<int:post_id>', methods=['PUT'])
def update_taste_rating(post_id):
    ratings_info = request.json
    rating_id = ratings_info['Rating_ID']
    post_id = ratings_info['Post_ID']
    user_id = ratings_info['User_ID']
    taste = ratings_info['taste']

    cursor = db.get_db().cursor()
    cursor.execute('UPDATE posts SET rating_id = %s, post_id = %s, user_id = %s, taste = %s', (new_taste_rating, post_id))
    db.get_db().commit()
    return 'taste rating updated!'

# Delete the rating on a post
@ratings.route('/ratings/<int:post_id>', methods=['DELETE'])
def delete_rating(post_id):
    cursor = db.get_db().cursor()
    cursor.execute('DELETE FROM ratings WHERE post_id = %s', (post_id,))
    db.get_db().commit()
    return make_response(jsonify({"message": "Rating deleted successfully"}), 200)

# Adding a new rating about the actual time to a post
@ratings.route('/ratings/<int:post_id>/<float:actual_time>', methods=['POST'])
def add_actual_time_rating(post_id, actual_time):
    ratings_info = request.json
    user_id = ratings_info['User_ID']

    cursor = db.get_db().cursor()
    cursor.execute('INSERT INTO ratings (post_id, user_id, actual_time) VALUES (%s, %s, %s)', (post_id, user_ID, actual_time))
    db.get_db().commit()
    return 'Successfully added new time rating!'

# Update average overall rating of actual time on a post
@ratings.route('/ratings/<int:post_id>/<float:actual_time>', methods=['PUT'])
def update_actual_time_rating(post_id, actual_time):
    ratings_info = request.json
    rating_id = ratings_info['Rating_ID']
    post_id = ratings_info['Post_ID']
    user_id = ratings_info['User_ID']
    actual_time = ratings_info['Actual_Time']

    cursor = db.get_db().cursor()
    cursor.execute('UPDATE ratings SET rating_id = %s, post_id = %s, user_id = %s, actual_time = %s', (new_rating_value, post_id, actual_time))
    db.get_db().commit()
    return 'time rating updated!'

# Adding a new rating about the actual difficulty to a post
@ratings.route('/ratings/<int:post_id>/<float:actual_difficulty>', methods=['POST'])
def add_actual_difficulty_rating(post_id, actual_difficulty):
    ratings_info = request.json
    user_id = ratings_info['User_ID']

    cursor = db.get_db().cursor()
    cursor.execute('INSERT INTO ratings (post_id, user_id, actual_difficulty) VALUES (%s, %s, %s)', (post_id, user_id, actual_difficulty))
    db.get_db().commit()
    return 'Successfully added difficulty rating!'

# Update average overall rating of actual difficulty on a post
@ratings.route('/ratings/<int:post_id>/<float:actual_difficulty>', methods=['PUT'])
def update_actual_difficulty_rating(post_id, actual_difficulty):
    ratings_info = request.json
    rating_id = ratings_info['Rating_ID']
    post_id = ratings_info['Post_ID']
    user_id = ratings_info['User_ID']
    actual_difficulty = rating_info['Actual_Difficulty']

    cursor = db.get_db().cursor()
    cursor.execute('UPDATE ratings SET rating_id = %s, post_id = %s, user_id = %s, actual_difficulty = %s', (new_rating_value, post_id, actual_difficulty))
    db.get_db().commit()
    return 'difficulty rating updated!'