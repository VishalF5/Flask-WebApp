from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson import ObjectId
import os

app = Flask(__name__)

# MongoDB Configuration
app.config["MONGO_URI"] = "mongodb://mongo:27017/users"
mongo = PyMongo(app)

# format documents
def format_user(user):
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "password": user["password"]
    }

# Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or not all(k in data for k in ("name", "email", "password")):
        return jsonify({"error": "Missing required fields"}), 400

    user = {
        "name": data["name"],
        "email": data["email"],
        "password": data["password"]
    }
    result = mongo.db.users.insert_one(user)
    return jsonify({"message": "User created", "id": str(result.inserted_id)}), 201

# Get all users
@app.route('/users', methods=['GET'])
def get_users():
    users = mongo.db.users.find()
    return jsonify([format_user(user) for user in users]), 200

# Get a user by ID
@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    try:
        user = mongo.db.users.find_one({"_id": ObjectId(id)})
        if user:
            return jsonify(format_user(user)), 200
        else:
            return jsonify({"error": "User not found"}), 404
    except:
        return jsonify({"error": "Invalid ID format"}), 400

# Update a user by ID
@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    update_data = {}
    for field in ["name", "email", "password"]:
        if field in data:
            update_data[field] = data[field]

    if not update_data:
        return jsonify({"error": "No valid fields to update"}), 400

    try:
        result = mongo.db.users.update_one({"_id": ObjectId(id)}, {"$set": update_data})
        if result.matched_count:
            return jsonify({"message": "User updated"}), 200
        else:
            return jsonify({"error": "User not found"}), 404
    except Exception as e:
        return jsonify({"error": e}), 400

# Delete a user by ID
@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    try:
        result = mongo.db.users.delete_one({"_id": ObjectId(id)})
        if result.deleted_count:
            return jsonify({"message": "User deleted"}), 200
        else:
            return jsonify({"error": "User not found"}), 404
    except:
        return jsonify({"error": "Invalid ID format"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
