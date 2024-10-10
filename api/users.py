from flask import Blueprint, jsonify, request
from pymongo.errors import PyMongoError
from werkzeug.security import check_password_hash, generate_password_hash

from api.models import Assignment, User

user_blueprint = Blueprint("users", __name__)


# User Registration
@user_blueprint.route("/register", methods=["POST"])
def register():
    """Create a new user
    username, password : Required fields
    """
    data = request.json
    if not data or "username" not in data or "password" not in data:
        return jsonify({"error": "Username and password are required."}), 400

    if User.find_by_username(data["username"]):
        return jsonify({"error": "Username already exists."}), 409

    try:
        hashed_password = generate_password_hash(data["password"])
        user = User(
            user_id=None,
            username=data["username"],
            password=hashed_password,
            role="user",
        )
        user.save()
        return jsonify({"message": "User registered successfully."}), 201
    except PyMongoError as e:
        return jsonify({"error": str(e)}), 500


# User Login
@user_blueprint.route("/login", methods=["POST"])
def login():
    """User Login"""
    data = request.json
    user = User.find_by_username(data["username"])
    if user and check_password_hash(user["password"], data["password"]):
        return (
            jsonify({"message": "Login successful.", "username": user["username"]}),
            200,
        )
    return jsonify({"msg": "Bad username or password"}), 401


# Upload Assignment
@user_blueprint.route("/upload", methods=["POST"])
def upload_assignment():
    """Uploads assigment
    task, admin : Required fields
    """
    data = request.json
    if not data or "task" not in data or "admin" not in data:
        return jsonify({"error": "Task and admin are required."}), 400

    assignment = Assignment(
        user_id=data["username"], task=data["task"], admin=data["admin"]
    )
    assignment.save()
    return jsonify({"message": "Assignment uploaded successfully."}), 201


# Fetch all Admins
@user_blueprint.route("/admins", methods=["GET"])
def fetch_admins():
    """Fetch all admins"""
    admins = User.find_admins()
    admin_list = [{"username": admin["username"]} for admin in admins]
    return jsonify(admin_list), 200
