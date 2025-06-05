from extensions import db

class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    budget = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    current_week = db.Column(db.Integer, default=1)
    budget_spent = db.Column(db.Float, default=0.0)
    status = db.Column(db.String(50), default="In Progress")

    # Убираем конфликтный relationship!
    # user = db.relationship('User', backref=db.backref('projects', lazy=True)) ❌ УБИРАЕМ
