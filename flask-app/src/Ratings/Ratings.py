from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

ratings = Blueprint('ratings', __name__)

# Add a new rating to a post
@ratings.route('/diff_rating', methods=['POST'])
def add_new_difficulty_rating():
    the_data = request.json
     # collecting data from the request object 
    current_app.logger.info(the_data)
    
    #extracting the variable
    rating_id = the_data['Rating_ID']
    actual_difficulty = the_data['Actual_Difficulty']
    actual_time = the_data['Actual_Time']
    taste = the_data['Taste']
    post_id = the_data['Post_ID']
    user_id = the_data['User_ID']

    # creating the query 
    query = 'insert into Ratings (Rating_ID, Actual_Difficulty, Actual_Time, Taste, Post_ID, User_ID) values ("'
    query += str(rating_id) + '", "'
    query += actual_difficulty + '", "'
    query += actual_time + '", "'
    query += taste + '", "'
    query += post_id + '", "'
    query += user_id + ')'
    current_app.logger.info(query)

     # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Successfully added difficulty rating!'




@ratings.route('/overall_rating', methods=['GET'])
def calculate_overall_rating():
    post_id = request.args.get('Post_ID')

    # Calculate the overall difficulty rating from the database
    query = "SELECT AVG(Actual_Difficulty) AS overall_rating FROM Ratings WHERE Post_ID = " + str(post_id)
    cursor = db.get_db().cursor()
    cursor.execute(query)
    overall_rating = cursor.fetchone()['overall_rating']

    return jsonify({'overall_rating': overall_rating})



@ratings.route('/o_diff_rating', methods=['PUT'])
def update_overall_diff_rating():
    filter_info = request.json
    post_id = filter_info['Post_ID']
    overall_difficulty_query = 'SELECT AVG(Actual_Difficulty) AS overall_difficulty \
                                FROM Ratings WHERE Post_ID = {post_id}'
    cursor = db.get_db().cursor
    cursor.execute(overall_difficulty_query)
    overall_difficulty = cursor.fetchone()['overall_difficulty']
    db.get_db().commit()
    return jsonify({'message': 'Successfully added difficulty rating!', 'overall_difficulty': overall_difficulty})



# Returns all ratings under a post
@ratings.route('/ratings/<post_id>', methods=['GET'])
def get_ratings(post_id):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Ratings WHERE Post_ID = %s', (post_id))
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
@ratings.route('/ratings/<post_id>/<taste>', methods=['PUT'])
def update_taste_rating(post_id, taste):
    ratings_info = request.json
    post_id = ratings_info['Post_ID']
    taste = ratings_info['taste']
    
    user_query = "SELECT User_ID FROM Users ORDER BY Created_At DESC LIMIT 1"
    current_app.logger.info(user_query)

    cursor = db.get_db().cursor()
    cursor.execute(user_query)
    user_result = cursor.fetchone()  # Fetch one row since we're expecting only one result
    user_id = user_result[0]  # Extract the user ID from the result

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

    user_query = "SELECT User_ID FROM Users ORDER BY Created_At DESC LIMIT 1"
    current_app.logger.info(user_query)

    cursor = db.get_db().cursor()
    cursor.execute(user_query)
    user_result = cursor.fetchone()  # Fetch one row since we're expecting only one result
    user_id = user_result[0]  # Extract the user ID from the result

    ratings_info = request.json

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
    actual_difficulty = ratings_info['Actual_Difficulty']



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












