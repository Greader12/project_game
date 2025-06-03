from flask import Blueprint, request, jsonify, session
from services.auth_service import register_user, authenticate_user

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/api/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    response, status = register_user(username, password)
    return jsonify(response), status

@auth_bp.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    response, status = authenticate_user(username, password)
    if status == 200:
        session["user_id"] = response["user_id"]
    return jsonify(response), status
