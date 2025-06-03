from flask import Blueprint, request, jsonify
from services.task_service import create_task, get_all_tasks

task_bp = Blueprint('task', __name__)

@task_bp.route("/api/tasks", methods=["POST"])
def create():
    data = request.get_json()
    name = data.get("name")
    base_duration = data.get("base_duration")
    base_cost = data.get("base_cost")
    project_id = data.get("project_id")
    start_week = data.get("start_week")

    if not name or base_duration is None or base_cost is None or not project_id or start_week is None:
        return jsonify({"error": "Missing task information"}), 400

    response, status = create_task(name, base_duration, base_cost, project_id, start_week)
    return jsonify(response), status

@task_bp.route("/api/tasks", methods=["GET"])
def get():
    tasks = get_all_tasks()
    return jsonify(tasks)
