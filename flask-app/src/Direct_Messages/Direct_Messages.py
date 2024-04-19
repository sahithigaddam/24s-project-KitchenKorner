# Direct messages 

from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db
# import os
# import mysql.connector

# # Get database connection details from environment variables
# # db_host = os.environ.get('DB_HOST')
# # db_user = os.environ.get('DB_USER')
# # db_password = os.environ.get('DB_PASSWORD')
# db_password = open('/secrets/db_root_password.txt').readline().strip()
# # db_name = os.environ.get('DB_NAME')

# # Connect to the MySQL database
# conn = mysql.connector.connect(
#     host='db',
#     user='root',
#     password=db_password,
#     database='Kitchen Korner'
# )
# cursor = conn.cursor()

# # Execute SQL query to fetch the most recent user ID
# cursor.execute("SELECT User_ID FROM Users ORDER BY Created_At DESC LIMIT 1")
# most_recent_user_id = cursor.fetchone()[0]  # Fetch the first column of the first row

# # Close the connection
# conn.close()

direct_messages = Blueprint('direct_messages', __name__)

@direct_messages.route('/direct_messages/<receiver_username>', methods=['GET'])
def get_receiver_id(receiver_username):  
    
    query = 'SELECT User_ID FROM Users WHERE Username = ' + '"' + str(receiver_username) + '"'
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    the_data = cursor.fetchall()
    for row in the_data:
        json_data.append(dict(zip(column_headers, row)))
    return jsonify(json_data)

@direct_messages.route('/direct_messages/<sender_id>', methods=['GET'])
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

# @direct_messages.route('/direct_messages', methods=['POST'])
# def send_direct_message():
 
#     # collecting data from the request object 
#     the_data = request.json
#     current_app.logger.info(the_data)

#     # extracting the variable
#     message = the_data['Message_Text']
#     receiver = the_data['Receiver_ID']

#     sender = "SELECT User_ID FROM Users ORDER BY Created_At DESC LIMIT 1"
#     current_app.logger.info(sender)
#     cursor = db.get_db().cursor()
#     cursor.execute(sender)
#     # column_headers = [x[0] for x in cursor.description]
#     # json_data = []
#     # the_data = cursor.fetchall()

#     # Constructing the query
#     query = 'INSERT INTO Direct_Messages (Message_Text, Receiver_ID, Sender_ID) VALUES ("'
#     query += message + '", "'
#     query += str(receiver) + '", "'
#     query += str(sender) + '")'

#     current_app.logger.info(query)

#     # executing and committing the insert statement 
#     cursor = db.get_db().cursor()
#     cursor.execute(query)
#     db.get_db().commit()
    
#     return 'Message Sent!'
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