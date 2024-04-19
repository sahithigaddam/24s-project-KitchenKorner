from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

ratings = Blueprint('ratings', __name__)

# Add a new exclusive filter
@ratings.route('/filters', methods=['POST'])
def add_new_filter_out():
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    filter_id = the_data['Filter_ID']
    keyword_one = the_data['Keyword_One']
    keyword_two = the_data['Keyword_Two']
    keyword_three = the_data['Keyword_Three']
    keyword_four = the_data['Keyword_Four']
    keyword_five= the_data['Keyword_Five']
    keyword_six = the_data['Keyword_Six']
    keyword_seven = the_data['Keyword_Seven']
    keyword_eight = the_data['Keyword_Eight']
    keyword_nine = the_data['Keyword_Nine']
    keyword_ten = the_data['Keyword_Ten']

    # creating the query 
    query = 'insert into Keywords_Out (Filter_ID, Keyword_One, Keyword_Two, Keyword_Three, Keyword_Four, Keyword_Five, Keyword_Six, Keyword_Seven, Keyword_Eight, Keyword_Nine, Keyword_Ten) values ("'
    query += str(filter_id) + '", "'
    query += keyword_one + '", "'
    query += keyword_two + '", "'
    query += keyword_three + '", "'
    query += keyword_four + '", "'
    query += keyword_five + '", "'
    query += keyword_six + '", "'
    query += keyword_seven + '", "'
    query += keyword_eight + '", "'
    query += keyword_nine + '", "'
    query += keyword_ten + ')'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Successfully added filter!'




















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






@filters.route('/filters', methods=['PUT'])
def update_keywords_in():
    filter_info = request.json
    filter_id = filter_info['Filter_ID']
    keyword_one = filter_info['Keyword_One']
    keyword_two = filter_info['Keyword_Two']
    keyword_three = filter_info['Keyword_Three']
    keyword_four = filter_info['Keyword_Four']
    keyword_five= filter_info['Keyword_Five']
    keyword_six = filter_info['Keyword_Six']
    keyword_seven = filter_info['Keyword_Seven']
    keyword_eight = filter_info['Keyword_Eight']
    keyword_nine = filter_info['Keyword_Nine']
    keyword_ten = filter_info['Keyword_Ten']

    query = 'UPDATE Keywords_In SET Keyword_One = %s, Keyword_Two = %s, Keyword_Three = %s, Keyword_Four = %s, Keyword_Five = %s, Keyword_Six = %s, Keyword_Seven = %s, Keyword_Eight = %s, Keyword_Nine = %s, Keyword_Ten = %s, where Filter_ID = %s'
    data = (keyword_one, keyword_two, keyword_three, keyword_four, keyword_five, keyword_six, keyword_seven, keyword_eight, keyword_nine, keyword_ten, filter_id)
    cursor = db.get_db().cursor()
    r = cursor.execute(query, data)
    db.get_db().commit()
    return 'Filter updated!'







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
    actual_difficulty = ratings_info['Actual_Difficulty']

    cursor = db.get_db().cursor()
    cursor.execute('UPDATE Ratings SET Rating_ID = %s, Post_ID = %s, User_ID = %s, Actual_Difficulty = %s', (New_Rating_Value, Post_ID, Actual_Difficulty))
    db.get_db().commit()
    return 'difficulty rating updated!'
