from flask import Blueprint, request, jsonify
from services.project_service import create_project, get_all_projects
from flask_jwt_extended import jwt_required

project_bp = Blueprint('project', __name__)

@project_bp.route("/api/projects", methods=["POST"])
@jwt_required()
def create():
    data = request.get_json()
    name = data.get("name")
    budget = data.get("budget")
    user_id = data.get("user_id")

    if not name or not budget or not user_id:
        return jsonify({"error": "Missing project information"}), 400

    response, status = create_project(name, budget, user_id)
    return jsonify(response), status

@project_bp.route("/api/projects", methods=["GET"])
@jwt_required()
def get():
    projects = get_all_projects()
    return jsonify(projects)
