# Direct messages 

from flask import Blueprint, request, jsonify, make_response
import json
from src import db

@direct_messages.route('/direct_messages/<sender_id>', methods=['GET'])
def get_direct_message(sender_id):
    cursor = db.get_db().cursor()
    query = "SELECT message FROM direct_messages WHERE sender_id = %s"
    cursor.execute(query, (sender_id,))
    message = cursor.fetchone()
    return make_response(jsonify({"message": message}), 200)

@direct_messages.route('/direct_messages', methods=['POST'])
def send_direct_message():
    data = request.get_json()
    cursor = db.get_db().cursor()
    query = "INSERT INTO direct_messages (sender_id, recipient_id, message) VALUES (%s, %s, %s)"
    cursor.execute(query, (data['sender_id'], data['recipient_id'], data['message']))
    db.get_db().commit()
    return make_response(jsonify({"message": "Direct message sent successfully"}), 201)