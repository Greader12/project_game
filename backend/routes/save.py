# app/routes/save.py
from flask_smorest import Blueprint
from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from extensions import db
from models.gamesave import GameSave
from flask.views import MethodView

blp = Blueprint("save", "save", url_prefix="/api/save", description="Save & Load game")

@blp.route("/save_game")
class SaveGame(MethodView):
    @jwt_required()
    def post(self):
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
        return {"message": "Game saved successfully."}, 200


@blp.route("/load_game")
class LoadGame(MethodView):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        save = GameSave.query.filter_by(user_id=user_id).first()
        if not save:
            return {"error": "No saved game found."}, 404

        return save.to_dict(), 200
