# utils/permissions.py

from flask_jwt_extended import get_jwt_identity
from models.user import User
from flask_smorest import abort
from functools import wraps

def admin_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        current_user_id = get_jwt_identity()
        user = User.query.get(current_user_id)
        if not user or user.role != 'admin':
            abort(403, message="Admin access required")
        return func(*args, **kwargs)
    return wrapper
