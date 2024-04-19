from flask import Blueprint, request, jsonify, make_response
import json
from src import db


ingredients = Blueprint('ingredients', __name__)

# Get all ingredients from the DB
@ingredients.route('/ingredients', methods=['GET'])
def get_ingredients():
    cursor = db.get_db().cursor()
    cursor.execute('select Amount, Ingredient_ID,\
        Price, Store, Ingredient_Name from Ingredients')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get all ingredient names from the DB
@ingredients.route('/ingredient_names', methods=['GET'])
def get_ingredient_names():
    cursor = db.get_db().cursor()
    cursor.execute('select Ingredient_Name from Ingredients')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# Get ingredient details
@ingredients.route('/ingredients/<Ingredient_ID>', methods=['GET'])
def get_ingredient(Ingredient_ID):
    cursor = db.get_db().cursor()
    cursor.execute('select * from Ingredients where Ingredient_ID = {0}'.format(Ingredient_ID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Add an ingredient
@ingredients.route('/ingredients', methods=['POST'])
def add_new_ingredient():
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    amount = the_data['Amount']
    price = the_data['Price']
    store = the_data['Store']
    name = the_data['Ingredient_Name']

    # Constructing the query
    query = 'insert into ingredients (amount, price, store, name) values ("'
    query += amount + '", "'
    query += str(price) + '", "'
    query += store + '", '
    query += name + ')'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'

# Update an ingredient
@ingredients.route('/ingredients/<Ingredient_ID>', methods=['PUT'])
def update_ingredient_price(Ingredient_ID):
    ingredient_info = request.json
    amount = ingredient_info['Amount']
    price = ingredient_info['Price']
    store = ingredient_info['Store']
    name = ingredient_info['Name']

    query = 'UPDATE Ingredients SET amount = %s, price = %s, store = %s,\
        name = %s where Ingredient_ID = %s'
    data = (amount, price, store, name, Ingredient_ID)
    cursor = db.get_db().cursor()
    r = cursor.execute(query, data)
    db.get_db().commit()
    return 'recipe updated!'