from flask import Blueprint, request, jsonify, make_response
import json
from src import db


recipes = Blueprint('Recipes', __name__)

# Get all customers from the DB
@recipes.route('/Recipes', methods=['GET'])
def get_recipes():
    cursor = db.get_db().cursor()
    cursor.execute('select Instructions, Meal_Type, Recipe_ID,\
        Post_ID, Cuisine, Expected_Time, Expected_Difficulty from Recipes')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get customer detail for customer with particular userID
@recipes.route('/recipes/<Recipe_ID>', methods=['GET'])
def get_recipe(Recipe_ID):
    cursor = db.get_db().cursor()
    cursor.execute('select * from Recipes where Recipe_ID = {0}'.format(Recipe_ID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@recipes.route('/recipes/<Recipe_ID>', methods=['PUT'])
def update_customers(Recipe_ID):
    recipe_info = request.json
    instructions = recipe_info['Instructions']
    image = recipe_info['Image']
    meal_type = recipe_info['Meal_Type']
    post_id = recipe_info['Post_ID']
    cuisine = recipe_info['Cuisine']
    time = recipe_info['Expected_Time']
    difficulty = recipe_info['Expected_Difficulty']

    query = 'UPDATE Recipes SET instructions = %s, image = %s, meal_type = %s,\
        post_id = %s, cuisine = %s, time = %s, difficulty = %s where Recipe_ID = %s'
    data = (instructions, image, meal_type, post_id, cuisine, time, difficulty, Recipe_ID)
    cursor = db.get_db().cursor()
    r = cursor.execute(query, data)
    db.get_db().commit()
    return 'recipe updated!'