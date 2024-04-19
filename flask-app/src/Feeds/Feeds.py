# Feeds

from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

feeds = Blueprint('feeds', __name__)


# Get the user's feed
@feeds.route('/feeds/<id>', methods=['GET'])
def get_feed(id):

    user_query = "SELECT User_ID FROM Users ORDER BY Created_At DESC LIMIT 1"
    current_app.logger.info(user_query)

    cursor = db.get_db().cursor()
    cursor.execute(user_query)
    user_result = cursor.fetchone()  # Fetch one row since we're expecting only one result
    id = user_result[0]  # Extract the user ID from the result

    query = 'SELECT Username, Recipe_Name, Recipe_Image, Meal_Type, Cuisine, Expected_Time, Expected_Difficulty FROM Recipes JOIN Posts ON Recipes.Post_ID = Posts.Post_ID JOIN Users ON Users.User_ID = Posts.User_ID'
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    the_data = cursor.fetchall()
    for row in the_data:
        json_data.append(dict(zip(column_headers, row)))
    return jsonify(json_data)