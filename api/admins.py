from flask import Blueprint, jsonify, request
from pymongo.errors import PyMongoError
from werkzeug.security import check_password_hash, generate_password_hash

from api.models import User

admin_blueprint = Blueprint("main", __name__)


# Admin Registration
@admin_blueprint.route("/admin/register", methods=["POST"])
def register_admin():
    """Create a new admin user
    username, password : Required fields
    """
    data = request.json

    # Check for required fields
    if not data or "username" not in data or "password" not in data:
        return jsonify({"error": "Username and password are required."}), 400

    # Check if user already exists
    if User.find_by_username(data["username"]):
        return jsonify({"error": "Username already exists."}), 409

    # Create new admin user
    try:
        hashed_password = generate_password_hash(data["password"])
        admin = User(
            user_id=None,
            username=data["username"],
            password=hashed_password,
            role="admin",
        )
        admin.save()
        return jsonify({"message": "Admin registered successfully."}), 201
    except PyMongoError as e:
        return jsonify({"error": str(e)}), 500


@admin_blueprint.route("/admin/login", methods=["POST"])
def login_admin():
    """Admin Login"""
    data = request.json

    # Get admin details
    admin = User.find_by_username(data["username"])

    # Verify password
    if admin and check_password_hash(admin["password"], data["password"]):
        return (
            jsonify({"message": "Login successful.", "username": admin["username"]}),
            200,
        )
    return jsonify({"msg": "Bad username or password"}), 401


@admin_blueprint.route("/users", methods=["GET"])
def get_users():
    """Get all users and their details"""
    users = User.find_users()
    return jsonify([User.format_user(user) for user in users]), 200


@admin_blueprint.route("/users/<id>", methods=["GET"])
def get_user(id):
    """Fetch User details by their ID"""
    try:
        user = User.get_user(id)
        if user:
            return jsonify(User.format_user(user)), 200
        else:
            return jsonify({"error": "User not found"}), 404
    except:
        return jsonify({"error": "Invalid ID format"}), 400


@admin_blueprint.route("/users/<id>", methods=["PUT"])
def update_user(id):
    """Update a user by ID"""
    data = request.json

    if not data:
        return jsonify({"error": "No data provided"}), 400

    update_data = {}
    for field in ["username", "password"]:
        if field in data:
            update_data[field] = data[field]

    if not update_data:
        return jsonify({"error": "No valid fields to update"}), 400

    try:
        result = User.update_user(id, update_data)
        if result.matched_count:
            return jsonify({"message": "User updated"}), 200
        else:
            return jsonify({"error": "User not found"}), 404
    except Exception as e:
        return jsonify({"error": e}), 400


@admin_blueprint.route("/users/<id>", methods=["DELETE"])
def delete_user(id):
    """Delete a user by ID"""
    try:
        result = User.delete_user(id)
        if result.deleted_count:
            return jsonify({"message": "User deleted"}), 200
        else:
            return jsonify({"error": "User not found"}), 404
    except:
        return jsonify({"error": "Invalid ID format"}), 400
