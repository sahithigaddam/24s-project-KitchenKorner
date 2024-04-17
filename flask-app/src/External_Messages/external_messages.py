# External messages 

from flask import Blueprint, request, jsonify, make_response
import json
from src import db

external_messages = Blueprint('external_messages', __name__)

@external_messages.route('/external_messages/<user_id>', methods=['GET'])
def get_external_message(user_id):
    cursor = db.get_db().cursor()
    query = "SELECT message FROM external_messages WHERE user_id = %s"
    cursor.execute(query, (user_id,))
    message = cursor.fetchone()
    return make_response(jsonify({"message": message}), 200)

@external_messages.route('/external_messages', methods=['POST'])
def send_external_message():
    data = request.get_json()
    cursor = db.get_db().cursor()
    query = "INSERT INTO external_messages (user_id, message) VALUES (%s, %s)"
    cursor.execute(query, (data['user_id'], data['message']))
    db.get_db().commit()
    return make_response(jsonify({"message": "External message sent successfully"}), 201)