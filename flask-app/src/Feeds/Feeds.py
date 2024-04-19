# External messages 

from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

feeds = Blueprint('feeds', __name__)


# Get the user's feed
@feeds.route('/feeds/<followee_id>', methods=['GET'])
def get_feed(followee_id):

    user_query = "SELECT User_ID FROM Users ORDER BY Created_At DESC LIMIT 1"
    current_app.logger.info(user_query)

    cursor = db.get_db().cursor()
    cursor.execute(user_query)
    user_result = cursor.fetchone()  # Fetch one row since we're expecting only one result
    followee_id = user_result[0]  # Extract the user ID from the result

    query = 'SELECT Posts.Post_ID, Username, Recipe_Name, Recipe_Image, Meal_Type, Cuisine, Expected_Time, Expected_Difficulty\
        FROM Users JOIN Feeds ON Feeds.User_ID = Users.User_ID\
        JOIN Follows ON Feeds.User_ID = Follows.Follower_ID\
        JOIN Posts ON Posts.User_ID = Follows.Followee_ID\
        JOIN Recipes ON Recipes.Post_ID = Posts.Post_ID WHERE Feeds.User_ID = ' + str(followee_id)
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    the_data = cursor.fetchall()
    for row in the_data:
        json_data.append(dict(zip(column_headers, row)))
    return jsonify(json_data)