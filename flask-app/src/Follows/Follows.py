# Follows

from flask import Blueprint, request, jsonify, make_response
import json
from src import db

follows = Blueprint('follows', __name__)

@follows.route('/follows/<followee_id>', methods=['GET'])
def get_followers(user_id):
    cursor = db.get_db().cursor()
    query = "SELECT Follower_ID FROM Follows WHERE Followee_ID = %s"
    cursor.execute(query, (user_id,))
    followers = cursor.fetchall()
    return make_response(jsonify({"followers": followers}), 200)

@follows.route('/follows', methods=['POST'])
def add_follower():
    data = request.get_json()
    cursor = db.get_db().cursor()
    query = "INSERT INTO Follows (Followee_ID, Follower_ID) VALUES (%s, %s)"
    cursor.execute(query, (data['Followee_ID'], data['Follower_ID']))
    db.get_db().commit()
    return make_response(jsonify({"message": "Follower added successfully"}), 201)

@follows.route('/follows', methods=['DELETE'])
def remove_follower():
    data = request.get_json()
    cursor = db.get_db().cursor()
    query = "DELETE FROM Follows WHERE Followee_ID = %s AND Follower_ID = %s"
    cursor.execute(query, (data['Followee_ID'], data['Follower_ID']))
    db.get_db().commit()
    return make_response(jsonify({"message": "Follower removed successfully"}), 200)
