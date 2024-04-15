# Users 

from flask import Blueprint, request, jsonify, make_response
import json
from src import db


users = Blueprint('customers', __name__)

# return a list of all users
@users.route('/users', methods=['GET'])
def get_users():
    cursor = db.get_db().cursor()
    cursor.execute('select company, last_name,\
        first_name, job_title, business_phone from customers')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Add a new user who joins the platform
@users.route('/users/add', methods=['POST'])
def add_user():
    data = request.get_json()
    cursor = db.get_db().cursor()
    query = "INSERT INTO customers (company, last_name, first_name, job_title, business_phone) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (data['company'], data['last_name'], data['first_name'], data['job_title'], data['business_phone']))
    db.get_db().commit()
    return make_response(jsonify({"message": "User added successfully"}), 201)