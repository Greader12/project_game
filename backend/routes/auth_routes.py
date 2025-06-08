from flask.views import MethodView
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, create_refresh_token
from flask_smorest import Blueprint
from werkzeug.security import generate_password_hash
from models.user import User
from extensions import db
from flask_smorest import abort
from flask_jwt_extended import get_jwt_identity
from marshmallow import Schema, fields
blp = Blueprint('auth', __name__, url_prefix='/api', description="Authentication operations")




class UserRegisterSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)

class UserLoginSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)

class TokenSchema(Schema):
    access_token = fields.Str()
    refresh_token = fields.Str()

@blp.route('/register')
class Register(MethodView):
    @blp.arguments(UserRegisterSchema)
    @blp.response(201, description="User created successfully")
    def post(self, user_data):
        if User.query.filter_by(username=user_data['username']).first():
            abort(400, message="User already exists")
        
        new_user = User(username=user_data['username'])
        new_user.set_password(user_data['password'])

        db.session.add(new_user)
        db.session.commit()

        return {"message": "User created successfully"}


@blp.route('/login')
class Login(MethodView):
    @blp.arguments(UserLoginSchema)
    @blp.response(200, TokenSchema)
    def post(self, login_data):
        user = User.query.filter_by(username=login_data['username']).first()

        if user and user.check_password(login_data['password']):  # ✅ Исправлено здесь
            access_token = create_access_token(identity=user.id)
            refresh_token = create_refresh_token(identity=user.id)
            return {
                "access_token": access_token,
                "refresh_token": refresh_token
            }
        abort(401, message="Invalid username or password")

@blp.route('/refresh')
class Refresh(MethodView):
    @jwt_required(refresh=True)
    @blp.doc(security=[{"BearerAuth": []}])  # <-- добавлено здесь!
    @blp.response(200, TokenSchema)
    def post(self):
        identity = get_jwt_identity()
        new_access_token = create_access_token(identity=identity)
        return {"access_token": new_access_token}