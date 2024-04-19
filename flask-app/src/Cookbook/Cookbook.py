from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


cookbook = Blueprint('cookbook', __name__)

# Get all cookbooks from the DB
@cookbook.route('/cookbook', methods=['GET'])
def get_cookbook():

    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list
    cursor.execute('SELECT c.Cookbook_Name, r.Recipe_Name, r.Meal_Type FROM Recipes r JOIN Cookbook c ON  r.Recipe_ID = c.Recipe_ID')

    # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

# Get cookbook name
@cookbook.route('/cname/<Cookbook_ID>', methods=['GET'])
def get_cookbook_name(Cookbook_ID):


    cursor = db.get_db().cursor()
   

# Get particular cookbook 
@cookbook.route('/cookbookrec/<Cookbook_ID>', methods=['GET'])
def get_cookbook_details(Cookbook_ID):
    query = 'SELECT Recipe_Name, Recipe_Image, Meal_Type, Cuisine, Expected_Time, Expected_Difficulty\
        FROM Cookbook JOIN Recipe_Cookbook ON Cookbook_ID = Recipe_Cookbook.Cookbook_ID\
        JOIN Recipes ON Recipe_Cookbook.Recipe_ID = Recipe_ID WHERE Cookbook.Cookbook_ID' + str(Cookbook_ID)
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    the_data = cursor.fetchall()
    for row in the_data:
        json_data.append(dict(zip(column_headers, row)))
    return jsonify(json_data)

# Add new cookbook
@cookbook.route('/cookbook', methods=['POST'])
def add_new_recipe():
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    recipe = the_data['Recipe_ID']
    cookbook_name = the_data['Cookbook_Name']

    # Query to get the user ID
    user_query = "SELECT User_ID FROM Users ORDER BY Created_At DESC LIMIT 1"
    current_app.logger.info(user_query)

    cursor = db.get_db().cursor()
    cursor.execute(user_query)
    user_result = cursor.fetchone()  # Fetch one row since we're expecting only one result
    user_id = user_result[0]  # Extract the user ID from the result

    # Constructing the query
    query = 'insert into Cookbook (Recipe_ID, User_ID, Cookbook_Name) values ("'
    query += recipe + '", "'
    query += user_id + '", "'
    query += cookbook_name + '")'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'