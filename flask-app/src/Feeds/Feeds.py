# External messages 

from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

feeds = Blueprint('feeds', __name__)


# Get the user's feed
@feeds.route('/feeds/<followee_id>', methods=['GET'])
def get_feed(followee_id):

    # Username, Recipe_Name, image, meal type, cuisine, expected time, expected difficulty
    # SELECT Followee_ID from Follows JOIN Feeds ON Feeds.User_ID = Follows.Follower_ID;
    # SELECT Post_ID from Posts JOIN [above query] ON Posts.User_ID = Follows.Followee_ID;
    # SELECT Username, Recipe_Name, Recipe_Image, Meal_Type, Cuisine, Expected_Time, Expected_Difficulty FROM Users JOIN Feeds ON Feeds.User_ID = Users.User_ID JOIN Follows ON Feeds.User_ID = Follows.Follower_ID JOIN Posts ON Posts.User_ID = Follows.Followee_ID JOIN Recipes ON Recipes/Post_ID = Posts.Post_ID;
    query = 'SELECT Posts.Post_ID, Username, Recipe_Name, Recipe_Image, Meal_Type,\
        Cuisine, Expected_Time, Expected_Difficulty FROM Users JOIN Feeds ON Feeds.User_ID = Users.User_ID\
        JOIN Follows ON Feeds.User_ID = Follows.Follower_ID\
        JOIN Posts ON Posts.User_ID = Follows.Followee_ID JOIN Recipes ON Recipes.Post_ID = Posts.Post_ID WHERE Feeds.User_ID = ' + str(user_id)
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    the_data = cursor.fetchall()
    for row in the_data:
        json_data.append(dict(zip(column_headers, row)))
    return jsonify(json_data)