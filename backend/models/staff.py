from models import db

class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100))    # например: "developer", "tester"
    speed = db.Column(db.Float)         # производительность
    cost = db.Column(db.Float)          # стоимость в день
    fatigue = db.Column(db.Integer, default=0)  # усталость
    morale = db.Column(db.Integer, default=100) # мораль
    xp = db.Column(db.Integer, default=0)       # опыт
    level = db.Column(db.Integer, default=1)    # уровень
    skill_upgrade = db.Column(db.String(100), default="")  # улучшения
