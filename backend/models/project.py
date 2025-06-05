from models.db import db

class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  # Название проекта
    budget = db.Column(db.Float, nullable=False)  # Бюджет проекта
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Связь с пользователем

    # ✅ Новые поля:
    current_week = db.Column(db.Integer, default=1)  # Текущая неделя проекта
    budget_spent = db.Column(db.Float, default=0.0)  # Сколько бюджета уже потрачено
    status = db.Column(db.String(50), default="In Progress")  # Статус проекта: In Progress, Completed, Failed

    user = db.relationship('User', backref=db.backref('projects', lazy=True))  # Связь обратно
