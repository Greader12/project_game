from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_smorest import Api
from config import Config
import os
from models import user, project, task, staff, assignment, event
from models import db
from services.schemas import ma
from errors import register_error_handlers

basedir = os.path.abspath(os.path.dirname(__file__))

jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    ma.init_app(app)

    cors = CORS(app, resources={
        r"/api/*": {
            "origins": [
                "http://localhost:3000",
                "https://yourgame.com"
            ],
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": ["Authorization", "Content-Type"],
        }
    })

    db.init_app(app)
    jwt.init_app(app)

    app.config['API_TITLE'] = 'Project Management Game API'
    app.config['API_VERSION'] = '1.0.0'
    app.config['OPENAPI_VERSION'] = '3.0.3'
    app.config['OPENAPI_URL_PREFIX'] = '/api/docs'
    app.config['OPENAPI_SWAGGER_UI_PATH'] = '/'
    app.config['OPENAPI_SWAGGER_UI_URL'] = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'

    api = Api(app)

    from routes.auth_routes import blp as AuthBlueprint
    from routes.project_routes import blp as ProjectBlueprint
    from routes.staff_routes import blp as StaffBlueprint
    from routes.task_routes import blp as TaskBlueprint
    from routes.assignment_routes import blp as AssignmentBlueprint


    api.register_blueprint(AuthBlueprint)
    api.register_blueprint(ProjectBlueprint)
    api.register_blueprint(StaffBlueprint)
    api.register_blueprint(TaskBlueprint)
    api.register_blueprint(AssignmentBlueprint)

    @jwt.user_identity_loader
    def user_identity_lookup(identity):
        return str(identity)

    migrate = Migrate(app, db)

    register_error_handlers(app)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
