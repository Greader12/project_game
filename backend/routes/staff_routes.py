from flask import Blueprint, request, jsonify
from services.staff_service import create_staff, get_all_staff, add_xp_to_staff, assign_skill_upgrade

from services.staff_service import (
    create_staff, get_all_staff, add_xp_to_staff, assign_skill_upgrade,
    add_fatigue_to_staff, rest_staff, get_effective_speed, trigger_random_event
)

staff_bp = Blueprint('staff', __name__)

@staff_bp.route("/api/staff", methods=["POST"])
def create():
    data = request.get_json()
    name = data.get("name")
    role = data.get("role")
    speed = data.get("speed")
    cost = data.get("cost")

    if not name or not role or speed is None or cost is None:
        return jsonify({"error": "Missing staff information"}), 400

    response, status = create_staff(name, role, speed, cost)
    return jsonify(response), status

@staff_bp.route("/api/staff", methods=["GET"])
def get():
    staff = get_all_staff()
    return jsonify(staff)

@staff_bp.route("/api/staff/<int:staff_id>/add_xp", methods=["POST"])
def add_xp(staff_id):
    data = request.get_json()
    xp_amount = data.get("xp_amount", 0)

    response, status = add_xp_to_staff(staff_id, xp_amount)
    return jsonify(response), status

@staff_bp.route("/api/staff/<int:staff_id>/assign_skill", methods=["POST"])
def assign_skill(staff_id):
    data = request.get_json()
    skill = data.get("skill")

    response, status = assign_skill_upgrade(staff_id, skill)
    return jsonify(response), status

@staff_bp.route("/api/staff/<int:staff_id>/add_fatigue", methods=["POST"])
def add_fatigue(staff_id):
    data = request.get_json()
    fatigue_amount = data.get("fatigue_amount", 0)

    response, status = add_fatigue_to_staff(staff_id, fatigue_amount)
    return jsonify(response), status

@staff_bp.route("/api/staff/<int:staff_id>/rest", methods=["POST"])
def rest(staff_id):
    response, status = rest_staff(staff_id)
    return jsonify(response), status

@staff_bp.route("/api/staff/<int:staff_id>/effective_speed", methods=["GET"])
def effective_speed(staff_id):
    response, status = get_effective_speed(staff_id)
    return jsonify(response), status

@staff_bp.route("/api/staff/<int:staff_id>/random_event", methods=["POST"])
def random_event(staff_id):
    response, status = trigger_random_event(staff_id)
    return jsonify(response), status