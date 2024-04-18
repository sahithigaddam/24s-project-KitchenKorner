# Direct messages 

from flask import Blueprint, request, jsonify, make_response
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
    data = request.form()
    cursor = db.get_db().cursor()
    query = "INSERT INTO Direct_Messages (Receiver_ID, Sender_ID, Message_Text, Time_Sent) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (data['Receiver_ID'], data['Sender_ID'], data['Message_Text'], data['Time_Sent']))
    db.get_db().commit()
    return make_response(jsonify({"message": "Direct message sent successfully"}))
