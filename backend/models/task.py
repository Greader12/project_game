from models.db import db

class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  # Название задачи
    difficulty = db.Column(db.Float, nullable=False)  # Сложность задачи
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)  # Связь с проектом

    # ✅ Новые поля:
    progress = db.Column(db.Float, default=0.0)  # Прогресс выполнения задачи от 0 до 100
    status = db.Column(db.String(50), default="In Progress")  # Статус задачи: In Progress, Completed, Failed

    project = db.relationship('Project', backref=db.backref('tasks', lazy=True))  # Связь обратно
