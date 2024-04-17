# Follows

from flask import Blueprint, request, jsonify, make_response
import json
from src import db

follows = Blueprint('follows', __name__)

# Get followers for particular user
@follows.route('/follows/<followee_id>', methods=['GET'])
def get_followers(user_id):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Follows WHERE Followee_ID = {0}'.format(user_id))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

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
