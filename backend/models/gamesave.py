# backend/models/gamesave.py
from extensions import db
from sqlalchemy.dialects.postgresql import JSON

class GameSave(db.Model):
    __tablename__ = "game_saves"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False, unique=True)
    week = db.Column(db.Integer, default=1)
    budget = db.Column(db.Integer, default=10000)
    staff = db.Column(JSON)
    tasks = db.Column(JSON)

    def to_dict(self):
        return {
            "week": self.week,
            "budget": self.budget,
            "staff": self.staff,
            "tasks": self.tasks
        }
