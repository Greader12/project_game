from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.project import Project
from models import db

project_bp = Blueprint('project', __name__, url_prefix='/api/projects')

@project_bp.route("/", methods=["GET"])
@jwt_required()
def get_projects():
    """
    Get list of projects
    ---
    tags:
      - Projects
    security:
      - bearerAuth: []
    responses:
      200:
        description: A list of projects
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                  name:
                    type: string
                  budget:
                    type: integer
                  user_id:
                    type: integer
      401:
        description: Unauthorized
    """
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
    """
    Create a new project
    ---
    tags:
      - Projects
    security:
      - bearerAuth: []
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            required:
              - name
              - budget
            properties:
              name:
                type: string
              budget:
                type: integer
    responses:
      201:
        description: Project created
      400:
        description: Missing name or budget
    """
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
