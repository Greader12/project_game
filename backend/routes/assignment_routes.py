from flask import Blueprint, request, jsonify
from models.assignment import Assignment
from models import db

assignment_bp = Blueprint('assignment', __name__)

@assignment_bp.route("/api/assignments", methods=["POST"])
def assign_staff():
    data = request.get_json()
    task_id = data.get("task_id")
    staff_id = data.get("staff_id")

    if not task_id or not staff_id:
        return jsonify({"error": "Missing task_id or staff_id"}), 400

    assignment = Assignment(task_id=task_id, staff_id=staff_id)
    db.session.add(assignment)
    db.session.commit()

    return jsonify({"message": "Staff assigned to task successfully"})

@assignment_bp.route("/api/assignments", methods=["GET"])
def get_assignments():
    assignments = Assignment.query.all()
    return jsonify([
        {
            "id": a.id,
            "task_id": a.task_id,
            "staff_id": a.staff_id
        }
        for a in assignments
    ])
