from flask import Blueprint, request, jsonify, make_response
import json
from src import db


ingredient_details = Blueprint('IngredientDetails', __name__)

# Get all customers from the DB
@ingredient_details.route('/IngredientDetails', methods=['GET'])
def get_ingredient_details():
    cursor = db.get_db().cursor()
    cursor.execute('select Recipe_ID, Ingredient_ID from IngredientDetails')
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
def get_customer(Recipe_ID):
    cursor = db.get_db().cursor()
    cursor.execute('select * from Recipes where Recipe_ID = {0}'.format(userID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response