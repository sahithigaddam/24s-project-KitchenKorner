from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


filters = Blueprint('filters', __name__)

# Get all the filtered in keywords from the database
@filters.route('/filters', methods=['GET'])
def get_keywords_in():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of keywords to filter into search
    cursor.execute('SELECT Filter_ID, Keyword_One, Keyword_Two, Keyword_Three, Keyword_Four, Keyword_Five, Keyword_Six, Keyword_Seven, Keyword_Eight, Keyword_Nine, Keyword_Ten FROM Keywords_In')

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


# Get all the filtered out keywords from the database
@filters.route('/filters', methods=['GET'])
def get_keywords_out():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT Filter_ID, Keyword_One, Keyword_Two, Keyword_Three, Keyword_Four, Keyword_Five, Keyword_Six, Keyword_Seven, Keyword_Eight, Keyword_Nine, Keyword_Ten FROM Keywords_Out')
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))
    return jsonify(json_data)



# Add a new inclusive filter 
@filters.route('/filters', methods=['POST'])
def add_new_filter_in():
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    filter_id = the_data['Filter_ID']
    keyword_one = the_data['Keyword_One']
    keyword_two = the_data['Keyword_Two']
    keyword_three = the_data['Keyword_Three']
    keyword_four = the_data['Keyword_Four']
    keyword_five= the_data['Keyword_Five']
    keyword_six = the_data['Keyword_Six']
    keyword_seven = the_data['Keyword_Seven']
    keyword_eight = the_data['Keyword_Eight']
    keyword_nine = the_data['Keyword_Nine']
    keyword_ten = the_data['Keyword_Ten']

    # creating the query 
    query = 'insert into Keywords_In (Filter_ID, Keyword_One, Keyword_Two, Keyword_Three, Keyword_Four, Keyword_Five, Keyword_Six, Keyword_Seven, Keyword_Eight, Keyword_Nine, Keyword_Ten) values ("'
    query += str(filter_id) + '", "'
    query += keyword_one + '", "'
    query += keyword_two + '", "'
    query += keyword_three + '", "'
    query += keyword_four + '", "'
    query += keyword_five + '", "'
    query += keyword_six + '", "'
    query += keyword_seven + '", "'
    query += keyword_eight + '", "'
    query += keyword_nine + '", "'
    query += keyword_ten + ')'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Successfully added filter!'

# Add a new exclusive filter
@filters.route('/filters', methods=['POST'])
def add_new_filter_out():
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    filter_id = the_data['Filter_ID']
    keyword_one = the_data['Keyword_One']
    keyword_two = the_data['Keyword_Two']
    keyword_three = the_data['Keyword_Three']
    keyword_four = the_data['Keyword_Four']
    keyword_five= the_data['Keyword_Five']
    keyword_six = the_data['Keyword_Six']
    keyword_seven = the_data['Keyword_Seven']
    keyword_eight = the_data['Keyword_Eight']
    keyword_nine = the_data['Keyword_Nine']
    keyword_ten = the_data['Keyword_Ten']

    # creating the query 
    query = 'insert into Keywords_Out (Filter_ID, Keyword_One, Keyword_Two, Keyword_Three, Keyword_Four, Keyword_Five, Keyword_Six, Keyword_Seven, Keyword_Eight, Keyword_Nine, Keyword_Ten) values ("'
    query += str(filter_id) + '", "'
    query += keyword_one + '", "'
    query += keyword_two + '", "'
    query += keyword_three + '", "'
    query += keyword_four + '", "'
    query += keyword_five + '", "'
    query += keyword_six + '", "'
    query += keyword_seven + '", "'
    query += keyword_eight + '", "'
    query += keyword_nine + '", "'
    query += keyword_ten + ')'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Successfully added filter!'

# Update an existing inclusive filter
@filters.route('/filters', methods=['PUT'])
def update_keywords_in():
    filter_info = request.json
    filter_id = filter_info['Filter_ID']
    keyword_one = filter_info['Keyword_One']
    keyword_two = filter_info['Keyword_Two']
    keyword_three = filter_info['Keyword_Three']
    keyword_four = filter_info['Keyword_Four']
    keyword_five= filter_info['Keyword_Five']
    keyword_six = filter_info['Keyword_Six']
    keyword_seven = filter_info['Keyword_Seven']
    keyword_eight = filter_info['Keyword_Eight']
    keyword_nine = filter_info['Keyword_Nine']
    keyword_ten = filter_info['Keyword_Ten']

    query = 'UPDATE Keywords_In SET Keyword_One = %s, Keyword_Two = %s, Keyword_Three = %s, Keyword_Four = %s, Keyword_Five = %s, Keyword_Six = %s, Keyword_Seven = %s, Keyword_Eight = %s, Keyword_Nine = %s, Keyword_Ten = %s, where Filter_ID = %s'
    data = (keyword_one, keyword_two, keyword_three, keyword_four, keyword_five, keyword_six, keyword_seven, keyword_eight, keyword_nine, keyword_ten, filter_id)
    cursor = db.get_db().cursor()
    r = cursor.execute(query, data)
    db.get_db().commit()
    return 'Filter updated!'

# Update an existing exclusive filter
@filters.route('/filters', methods=['PUT'])
def update_keywords_out():
    filter_info = request.json
    filter_id = filter_info['Filter_ID']
    keyword_one = filter_info['Keyword_One']
    keyword_two = filter_info['Keyword_Two']
    keyword_three = filter_info['Keyword_Three']
    keyword_four = filter_info['Keyword_Four']
    keyword_five= filter_info['Keyword_Five']
    keyword_six = filter_info['Keyword_Six']
    keyword_seven = filter_info['Keyword_Seven']
    keyword_eight = filter_info['Keyword_Eight']
    keyword_nine = filter_info['Keyword_Nine']
    keyword_ten = filter_info['Keyword_Ten']

    query = 'UPDATE Keywords_Out SET Keyword_One = %s, Keyword_Two = %s, Keyword_Three = %s, Keyword_Four = %s, Keyword_Five = %s, Keyword_Six = %s, Keyword_Seven = %s, Keyword_Eight = %s, Keyword_Nine = %s, Keyword_Ten = %s, where Filter_ID = %s'
    data = (keyword_one, keyword_two, keyword_three, keyword_four, keyword_five, keyword_six, keyword_seven, keyword_eight, keyword_nine, keyword_ten, filter_id)
    cursor = db.get_db().cursor()
    r = cursor.execute(query, data)
    db.get_db().commit()
    return 'Filter updated!'


# Delete an inclusive filter 
@filters.route('/filters/<Filter_ID>', methods=['DELETE'])
def delete_filter_in(Filter_ID):
    cursor = db.get_db().cursor()
    query = "DELETE FROM Keywords_In WHERE Filter_ID = %s"
    cursor.execute(query, (Filter_ID,))
    query1 = "DELETE FROM Filters WHERE Filter_ID = %s"      # also deleting in filters table
    cursor.execute(query1, (Filter_ID))       # also deleting in filters table
    db.get_db().commit()
    return make_response(jsonify({"message": "Filter deleted successfully"}), 200)

# Delete an exclusive filter 
@filters.route('/filters/<Filter_ID>', methods=['DELETE'])
def delete_filter_out(Filter_ID):
    cursor = db.get_db().cursor()
    query = "DELETE FROM Keywords_Out WHERE Filter_ID = %s"
    cursor.execute(query, (Filter_ID,))
    query = "DELETE FROM Filters WHERE Filter_ID = %s"      # also deleting in filters table
    cursor.execute(query, (Filter_ID))      # also deleting in filters table
    db.get_db().commit()
    return make_response(jsonify({"message": "Filter deleted successfully"}), 200)


