# Direct messages 

from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

direct_messages = Blueprint('direct_messages', __name__)

@direct_messages.route('/direct_messages/<sender_id>', methods=['GET'])
def get_direct_message(sender_id):
    cursor = db.get_db().cursor()
    query = "SELECT Message_Text FROM Direct_Messages WHERE Sender_ID = %s"
    cursor.execute(query, (sender_id,))
    message = cursor.fetchone()
    return make_response(jsonify({"message": message}))


@direct_messages.route('/direct_messages', methods=['POST'])
def send_direct_message():
 
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    message = the_data['Message_Text']
    receiver = the_data['Receiver_Username']

    # Constructing the query
    query = 'insert into Direct_Messages (Message_Text, Receiver_Username) values ("'
    query += message + '", "'
    query += str(receiver) + '")'

    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Message Sent!'
