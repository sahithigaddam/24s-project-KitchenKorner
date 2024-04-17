from flask import Blueprint, request, jsonify, make_response
import json
from src import db

ratings = Blueprint('ratings', __name__)

# Returns all ratings under a post
@ratings.route('/ratings/<post_id>', methods=['GET'])
def get_ratings(post_id):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Ratings WHERE Post_ID = %s', (Post_ID))
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
@ratings.route('/ratings/<post_id>', methods=['PUT'])
def update_taste_rating(post_id):
    ratings_info = request.json
    rating_id = ratings_info['Rating_ID']
    post_id = ratings_info['Post_ID']
    user_id = ratings_info['User_ID']
    taste = ratings_info['taste']

    cursor = db.get_db().cursor()
    cursor.execute('UPDATE Posts SET Rating_ID = %s, Post_ID = %s, User_ID = %s, Taste = %s', (New_Taste_Rating, Post_ID))
    db.get_db().commit()
    return 'taste rating updated!'

# Delete the rating on a post
@ratings.route('/ratings/<post_id>', methods=['DELETE'])
def delete_rating(post_id):
    cursor = db.get_db().cursor()
    cursor.execute('DELETE FROM Ratings WHERE Post_ID = %s', (Post_ID))
    db.get_db().commit()
    return make_response(jsonify({"message": "Rating deleted successfully"}), 200)

# Adding a new rating about the actual time to a post
@ratings.route('/ratings/<post_id>/<actual_time>', methods=['POST'])
def add_actual_time_rating(post_id, actual_time):
    ratings_info = request.json
    user_id = ratings_info['User_ID']

    cursor = db.get_db().cursor()
    cursor.execute('INSERT INTO Ratings (Post_ID, User_ID, Actual_Time) VALUES (%s, %s, %s)', (Post_ID, User_ID, Actual_Time))
    db.get_db().commit()
    return 'Successfully added new time rating!'

# Update average overall rating of actual time on a post
@ratings.route('/ratings/<post_id>/<actual_time>', methods=['PUT'])
def update_actual_time_rating(post_id, actual_time):
    ratings_info = request.json
    rating_id = ratings_info['Rating_ID']
    post_id = ratings_info['Post_ID']
    user_id = ratings_info['User_ID']
    actual_time = ratings_info['Actual_Time']

    cursor = db.get_db().cursor()
    cursor.execute('UPDATE Ratings SET Rating_ID = %s, Post_ID = %s, User_ID = %s, Actual_Time = %s', (New_Rating_Value, Post_ID, Actual_Time))
    db.get_db().commit()
    return 'time rating updated!'

# Adding a new rating about the actual difficulty to a post
@ratings.route('/ratings/<post_id>/<actual_difficulty>', methods=['POST'])
def add_actual_difficulty_rating(post_id, actual_difficulty):
    ratings_info = request.json
    user_id = ratings_info['User_ID']

    cursor = db.get_db().cursor()
    cursor.execute('INSERT INTO Ratings (Post_ID, User_ID, Actual_Difficulty) VALUES (%s, %s, %s)', (Post_ID, User_ID, Actual_Difficulty))
    db.get_db().commit()
    return 'Successfully added difficulty rating!'

# Update average overall rating of actual difficulty on a post
@ratings.route('/ratings/<post_id>/<actual_difficulty>', methods=['PUT'])
def update_actual_difficulty_rating(post_id, actual_difficulty):
    ratings_info = request.json
    rating_id = ratings_info['Rating_ID']
    post_id = ratings_info['Post_ID']
    user_id = ratings_info['User_ID']
    actual_difficulty = rating_info['Actual_Difficulty']

    cursor = db.get_db().cursor()
    cursor.execute('UPDATE Ratings SET Rating_ID = %s, Post_ID = %s, User_ID = %s, Actual_Difficulty = %s', (New_Rating_Value, Post_ID, Actual_Difficulty))
    db.get_db().commit()
    return 'difficulty rating updated!'
