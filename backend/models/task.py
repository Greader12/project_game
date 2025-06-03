from models import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    base_duration = db.Column(db.Integer, nullable=False)
    base_cost = db.Column(db.Integer, nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    start_week = db.Column(db.Integer, nullable=False)

    project = db.relationship('Project', backref=db.backref('tasks', lazy=True))
