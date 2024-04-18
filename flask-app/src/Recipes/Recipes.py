from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


recipes = Blueprint('recipes', __name__)

# Get all recipes from the DB
@recipes.route('/recipes', methods=['GET'])
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

# Fix so that Posts_ID is inputted Recipe_ID
# Get recipe details
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
    # image = recipe_info['Image']
    meal_type = recipe_info['Meal_Type']
    post_id = recipe_info['Post_ID']
    cuisine = recipe_info['Cuisine']
    time = recipe_info['Expected_Time']
    difficulty = recipe_info['Expected_Difficulty']

    query = 'UPDATE Recipes SET Instructions = %s, Meal_Type = %s,\
        Post_ID = %s, Cuisine = %s, Expected_Time = %s, Expected_Difficulty = %s where Recipe_ID = %s'
    data = (instructions, meal_type, post_id, cuisine, time, difficulty, Recipe_ID)
    cursor = db.get_db().cursor()
    r = cursor.execute(query, data)
    db.get_db().commit()
    return 'recipe updated!'

# Add a new recipe
@recipes.route('/recipes', methods=['POST'])
def add_new_recipe():
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    meal_type = the_data['Meal_Type']
    cuisine = the_data['Cuisine']
    time = the_data['Expected_Time']
    difficulty = the_data['Expected_Difficulty']

    # Constructing the query
    query = 'insert into Recipes (Meal_Type, Cuisine, Expected_Time, Expected_Difficulty) values ("'
    query += meal_type + '", "'
    query += cuisine + '", "'
    query += str(time) + '", "'
    query += str(difficulty) + '")'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'

# Route to filter recipes based on selected ingredients
@recipes.route('/recipes', methods=['GET'])
def filter_recipes():
    selected_ingredients = request.args.getlist('ingredients')

    # Construct SQL query to filter recipes by selected ingredients
    query = """
    SELECT r.Recipe_ID, r.Recipe_Name, r.Meal_Type, r.Cuisine
    FROM Recipes r
    INNER JOIN Ingredient_Details id ON r.Recipe_ID = id.Recipe_ID
    INNER JOIN Ingredients i ON id.Ingredient_ID = i.Ingredient_ID
    WHERE i.Ingredient_Name IN (%s)
    GROUP BY r.Recipe_ID
    """

    # Execute the SQL query
    cursor = db.cursor()
    cursor.execute(query, (selected_ingredients,))
    filtered_recipes = cursor.fetchall()

    # Convert results to JSON format
    recipes_json = []
    for recipe in filtered_recipes:
        recipe_json = {
            'Recipe_ID': recipe[0],
            'Recipe_Name': recipe[1],
            'Meal_Type': recipe[2],
            'Cuisine': recipe[3]
        }
        recipes_json.append(recipe_json)

    cursor.close()
    return jsonify(recipes_json)