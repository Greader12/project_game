# app/routes/save.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.extensions import db
from app.models.gamesave import GameSave

save_bp = Blueprint("save", __name__)

@save_bp.route("/save_game", methods=["POST"])
@jwt_required()
def save_game():
    user_id = get_jwt_identity()
    data = request.get_json()

    existing_save = GameSave.query.filter_by(user_id=user_id).first()
    if existing_save:
        existing_save.week = data.get("week", 1)
        existing_save.budget = data.get("budget", 10000)
        existing_save.staff = data.get("staff", [])
        existing_save.tasks = data.get("tasks", [])
    else:
        new_save = GameSave(
            user_id=user_id,
            week=data.get("week", 1),
            budget=data.get("budget", 10000),
            staff=data.get("staff", []),
            tasks=data.get("tasks", [])
        )
        db.session.add(new_save)

    db.session.commit()
    return jsonify({"message": "Game saved successfully."}), 200

@save_bp.route("/load_game", methods=["GET"])
@jwt_required()
def load_game():
    user_id = get_jwt_identity()
    save = GameSave.query.filter_by(user_id=user_id).first()
    if not save:
        return jsonify({"error": "No saved game found."}), 404

    return jsonify(save.to_dict()), 200
