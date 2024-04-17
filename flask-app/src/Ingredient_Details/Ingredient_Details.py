from flask import Blueprint, request, jsonify, make_response
import json
from src import db


ingredient_details = Blueprint('ingredient_details', __name__)

# Get all customers from the DB
@ingredient_details.route('/ingredient_details', methods=['GET'])
def get_ingredient_details():
    cursor = db.get_db().cursor()
    cursor.execute('select Recipe_ID, Ingredient_ID from Ingredient_Details')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# TODO: FIX
# Get customer detail for customer with particular userID
@ingredient_details.route('/ingredient_details/<Recipe_ID>', methods=['GET'])
def get_ingredient(Recipe_ID):
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

@ingredient_details.route('/ingredient_details/<Recipe_ID>', methods=['GET'])
def get_ingredients_for_recipe(Recipe_ID):
    cursor = db.get_db().cursor()
    cursor.execute('''
        SELECT Ingredients.* 
        FROM Ingredient_Details 
        JOIN Ingredients ON Ingredient_Details.Ingredient_ID = Ingredients.Ingredient_ID 
        WHERE Ingredient_Details.Recipe_ID = %s
    ''', (Recipe_ID,))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response
