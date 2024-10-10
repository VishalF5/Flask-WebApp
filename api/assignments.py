from flask import Blueprint, jsonify, request

from api.models import Assignment

assignment_blueprint = Blueprint("assignment", __name__)


@assignment_blueprint.route("/assignments", methods=["GET"])
def view_assignments():
    """View Assignments tagged to current admin"""
    current_admin = request.args.get("username")
    assignments = Assignment.find_by_admin(current_admin)
    return jsonify(assignments), 200


@assignment_blueprint.route("/assignments/<id>/accept", methods=["POST"])
def accept_assignment(id):
    """Accept Assignment"""
    try:
        Assignment.update_status(id, "accepted")
        return jsonify({"message": "Assignment accepted."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@assignment_blueprint.route("/assignments/<id>/reject", methods=["POST"])
def reject_assignment(id):
    """Reject Assignment"""
    try:
        Assignment.update_status(id, "rejected")
        return jsonify({"message": "Assignment rejected."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
