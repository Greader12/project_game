from models.user import User
from models import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

def register_user(username, password):
    existing_user = User.query.filter_by(username=username).first()

    if existing_user:
        return {"error": "Username already exists."}, 409

    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password_hash=hashed_password)

    db.session.add(new_user)
    db.session.commit()

    return {"message": "User registered successfully."}, 201

def authenticate_user(username, password):
    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password_hash, password):
        return {"error": "Invalid username or password."}, 401

    # Создание JWT токена
    access_token = create_access_token(identity=str(user.id))


    return {"access_token": access_token}, 200
