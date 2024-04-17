# Follows

from flask import Blueprint, request, jsonify, make_response
import json
from src import db

follows = Blueprint('Follows', __name__)

@follows.route('/followers/followee_id>', methods=['GET'])
def get_followers(user_id):
    cursor = db.get_db().cursor()
    query = "SELECT follower_id FROM follows WHERE user_id = %s"
    cursor.execute(query, (user_id,))
    followers = cursor.fetchall()
    return make_response(jsonify({"followers": followers}), 200)

@follows.route('/followers', methods=['POST'])
def add_follower():
    data = request.get_json()
    cursor = db.get_db().cursor()
    query = "INSERT INTO follows (user_id, follower_id) VALUES (%s, %s)"
    cursor.execute(query, (data['user_id'], data['follower_id']))
    db.get_db().commit()
    return make_response(jsonify({"message": "Follower added successfully"}), 201)

@follows.route('/followers', methods=['DELETE'])
def remove_follower():
    data = request.get_json()
    cursor = db.get_db().cursor()
    query = "DELETE FROM follows WHERE user_id = %s AND follower_id = %s"
    cursor.execute(query, (data['user_id'], data['follower_id']))
    db.get_db().commit()
    return make_response(jsonify({"message": "Follower removed successfully"}), 200)