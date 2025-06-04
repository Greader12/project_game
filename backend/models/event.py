from models import db

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)  # Название события
    description = db.Column(db.Text, nullable=False)  # Описание события
    effect_type = db.Column(db.String(50), nullable=False)  # Тип эффекта: delay, cost_increase, morale_drop
    effect_value = db.Column(db.Float, nullable=False)  # Величина эффекта (например, +20%)
    probability = db.Column(db.Float, nullable=False)  # Вероятность выпадения события (0.2 = 20%)