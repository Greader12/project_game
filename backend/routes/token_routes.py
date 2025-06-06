from flask.views import MethodView
from flask_smorest import Blueprint
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity

blp = Blueprint('token', __name__, url_prefix='/api/token', description="Token operations")

@blp.route('/refresh')
class TokenRefresh(MethodView):
    @jwt_required(refresh=True)
    def post(self):
        identity = get_jwt_identity()
        access_token = create_access_token(identity=identity)
        return {'access_token': access_token}
