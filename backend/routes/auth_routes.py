from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from services.auth_service import register_user, authenticate_user

auth_bp = Blueprint('auth', __name__, url_prefix='/api')

@auth_bp.route("/register", methods=["POST"])
def register():
    """
    User registration
    ---
    tags:
      - Auth
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            required:
              - username
              - password
            properties:
              username:
                type: string
              password:
                type: string
    responses:
      201:
        description: User registered successfully
      409:
        description: Username already exists
    """
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    response, status = register_user(username, password)
    return jsonify(response), status

@auth_bp.route("/login", methods=["POST"])
def login():
    """
    User login
    ---
    tags:
      - Auth
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            required:
              - username
              - password
            properties:
              username:
                type: string
              password:
                type: string
    responses:
      200:
        description: Login successful
      401:
        description: Invalid credentials
    """
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    response, status = authenticate_user(username, password)
    return jsonify(response), status

@auth_bp.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    """
    Refresh access token
    ---
    tags:
      - Auth
    security:
      - bearerAuth: []
    responses:
      200:
        description: New access token issued
      401:
        description: Invalid or expired refresh token
    """
    identity = get_jwt_identity()
    new_access_token = create_access_token(identity=identity)
    return jsonify(access_token=new_access_token), 200
