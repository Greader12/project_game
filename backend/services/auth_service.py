from models.user import User
from models import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

def register_user(username, password):
    if User.query.filter_by(username=username).first():
        return {"error": "User already exists"}, 409

    user = User(username=username, password_hash=generate_password_hash(password))
    db.session.add(user)
    db.session.commit()
    return {"message": "User registered successfully"}, 201

def authenticate_user(username, password):
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password_hash, password):
        access_token = create_access_token(identity=user.id, expires_delta=timedelta(hours=1))
        return {"access_token": access_token}, 200
    else:
        return {"error": "Invalid credentials"}, 401