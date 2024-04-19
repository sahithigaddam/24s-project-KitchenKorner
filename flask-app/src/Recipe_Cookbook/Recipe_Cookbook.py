from flask import Blueprint, request, jsonify, make_response
import json
from src import db


recipe_cookbook = Blueprint('recipe_cookbook', __name__)

# Get recipe_details
@recipe_cookbook.route('/recipe_cookbook', methods=['GET'])
def get_recipe_cookbook():
    cursor = db.get_db().cursor()
    cursor.execute('select Recipe_ID, Cookbook_ID from Recipe_Cookbook')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response