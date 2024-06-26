# Direct messages 

from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

direct_messages = Blueprint('direct_messages', __name__)

# Get direct messages for a specific user
@direct_messages.route('/direct_messages/<receiver_id>', methods=['GET'])
def get_receiver_id(receiver_id):  
    
    user_query = "SELECT User_ID FROM Users ORDER BY Created_At DESC LIMIT 1"
    current_app.logger.info(user_query)

    cursor = db.get_db().cursor()
    cursor.execute(user_query)
    user_result = cursor.fetchone()  # Fetch one row since we're expecting only one result
    user_id = user_result[0]  # Extract the user ID from the result

    query = 'SELECT Message_Text, Time_Sent FROM Direct_Messages WHERE Receiver_ID IN (\
        ' + str(receiver_id) + ', ' + str(user_id) + ') AND Sender_ID IN (' + str(user_id) + ', ' + str(receiver_id) + ')'
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    the_data = cursor.fetchall()
    for row in the_data:
        json_data.append(dict(zip(column_headers, row)))
    return jsonify(json_data)

# Get direct messages
@direct_messages.route('/dm/<sender_id>', methods=['GET'])
def get_direct_message(sender_id):

    query = 'SELECT Message_Text FROM Direct_Messages WHERE Sender_ID = ' + str(sender_id)
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    the_data = cursor.fetchall()
    for row in the_data:
        json_data.append(dict(zip(column_headers, row)))
    return jsonify(json_data)

# Send message to user on app
@direct_messages.route('/direct_messages', methods=['POST'])
def send_direct_message():
    # Collecting data from the request object
    the_data = request.json
    current_app.logger.info(the_data)

    # Extracting the variable
    message = the_data['Message_Text']
    receiver = the_data['Receiver_ID']

    # Query to get the sender ID
    sender_query = "SELECT User_ID FROM Users ORDER BY Created_At DESC LIMIT 1"
    current_app.logger.info(sender_query)

    cursor = db.get_db().cursor()
    cursor.execute(sender_query)
    sender_result = cursor.fetchone()  # Fetch one row since we're expecting only one result
    sender_id = sender_result[0]  # Extract the sender ID from the result

    # Constructing the query
    query = 'INSERT INTO Direct_Messages (Message_Text, Receiver_ID, Sender_ID) VALUES (%s, %s, %s)'
    values = (message, receiver, sender_id)

    current_app.logger.info(query)
    current_app.logger.info(values)

    # Executing and committing the insert statement
    cursor.execute(query, values)
    db.get_db().commit()

    return 'Message Sent!'