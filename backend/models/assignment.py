from extensions import db


class Assignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'), nullable=False)
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=False)

    task = db.relationship('Task', backref=db.backref('assignments', lazy=True))
    staff = db.relationship('Staff', backref=db.backref('assignments', lazy=True))
