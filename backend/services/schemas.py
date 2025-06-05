from flask_marshmallow import Marshmallow
from marshmallow import fields, validate

ma = Marshmallow()

# ✅ Схема для регистрации и логина пользователя
class UserSchema(ma.Schema):
    username = fields.Str(required=True, validate=validate.Length(min=3, max=150))
    password = fields.Str(required=True, validate=validate.Length(min=6))

# ✅ Схема для создания проекта
class ProjectSchema(ma.Schema):
    name = fields.Str(required=True, validate=validate.Length(min=2))
    budget = fields.Integer(required=True, validate=validate.Range(min=0))
