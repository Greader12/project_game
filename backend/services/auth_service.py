from models.user import User
from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_smorest import abort
def register_user(data):
    username = data.get('username')
    password = data.get('password')

    if User.query.filter_by(username=username).first():
        abort(400, message="User already exists")

    new_user = User(username=username)
    new_user.set_password(password)  # Установить пароль с шифрованием

    db.session.add(new_user)
    db.session.commit()
    return new_user

def login_user(data):
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if user and user.check_password(password):
        access_token = create_access_token(identity=user.id)
        refresh_token = create_refresh_token(identity=user.id)
        return {'access_token': access_token, 'refresh_token': refresh_token}

    abort(401, message="Invalid credentials")