    # Cookbook_ID int PRIMARY KEY,
    # Recipe_ID int NOT NULL,
    # User_ID int NOT NULL,
    # Modified_Datetime datetime,

from flask import Blueprint, request, jsonify, make_response
import json
from src import db


cookbook = Blueprint('Cookbook', __name__)

# Get all customers from the DB
@cookbook.route('/Cookbook', methods=['GET'])
def get_cookbook():
    cursor = db.get_db().cursor()
    cursor.execute('select Cookbook_ID, Recipe_ID, User_ID, Modified_Datetime from Cookbook')
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
@cookbook.route('/cookbook/<Cookbook_ID>', methods=['GET'])
def get_cookbook_details(Cookbook_ID):
    cursor = db.get_db().cursor()
    cursor.execute('select * from Cookbook where Cookbook_ID = {0}'.format(Cookbook_ID))
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
# Adding a new recipe to the cookbook
@cookbook.route('/cookbook/<Cookbook_ID', methods=['POST'])
def add_new_recipe(Cookbook_ID):
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    name = the_data['product_name']
    description = the_data['product_description']
    price = the_data['product_price']
    category = the_data['product_category']

    # Constructing the query
    query = 'insert into cookbook (product_name, description, category, list_price) values ("'
    query += name + '", "'
    query += description + '", "'
    query += category + '", '
    query += str(price) + ')'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'
