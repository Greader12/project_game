from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.project import Project
from models import db

project_bp = Blueprint('project', __name__, url_prefix='/api/projects')

@project_bp.route("/", methods=["GET"])
@jwt_required()
def get_projects():
    projects = Project.query.all()
    project_list = [
        {
            "id": project.id,
            "name": project.name,
            "budget": project.budget,
            "user_id": project.user_id
        }
        for project in projects
    ]
    return jsonify(project_list), 200

@project_bp.route("/", methods=["POST"])
@jwt_required()
def create_project():
    data = request.get_json()
    name = data.get("name")
    budget = data.get("budget")

    if not name or not budget:
        return jsonify({"error": "Missing name or budget."}), 400

    user_id = get_jwt_identity()
    new_project = Project(name=name, budget=budget, user_id=user_id)

    db.session.add(new_project)
    db.session.commit()

    return jsonify({"message": "Project created successfully."}), 201
