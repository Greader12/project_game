from models.user import User
from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token

def register_user(data):
    username = data.get('username')
    password = data.get('password')

    if User.query.filter_by(username=username).first():
        raise Exception('User already exists')

    new_user = User(username=username)
    new_user.set_password(password)  # Установить пароль с шифрованием

    db.session.add(new_user)
    db.session.commit()
    return new_user

def login_user(data):
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if user and user.check_password(password):  # ✅ Проверяем пароль через метод
        # логика генерации токена
        access_token = create_access_token(identity=user.id)
        return {'access_token': access_token}

    raise Exception('Invalid credentials')