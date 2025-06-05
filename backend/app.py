from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flasgger import Swagger  # 🚀 Swagger импортируем
from config import Config
import os
from models import user, project, task, staff, assignment, event
from models import db
from schemas import ma  # Marshmallow
from errors import register_error_handlers  # Глобальный обработчик ошибок

basedir = os.path.abspath(os.path.dirname(__file__))

jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Init Marshmallow
    ma.init_app(app)

    # CORS настройка
    cors = CORS(app, resources={
        r"/api/*": {
            "origins": [
                "http://localhost:3000",       # Фронт локальный
                "https://yourgame.com"         # Продакшн домен (заменишь позже)
            ],
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": ["Authorization", "Content-Type"],
        }
    })

    db.init_app(app)
    jwt.init_app(app)

    # 🚀 Swagger подключаем ТОЛЬКО в режиме разработки
    if app.config["ENV"] == "development":
        Swagger(app, template={
            "swagger": "2.0",
            "info": {
                "title": "Project Management API",
                "description": "API for user registration, login, and project management",
                "version": "1.0"
            },
            "securityDefinitions": {
                "bearerAuth": {
                    "type": "apiKey",
                    "name": "Authorization",
                    "in": "header",
                    "description": "Enter: **Bearer &lt;JWT&gt;**"
                }
            },
        })

    @jwt.user_identity_loader
    def user_identity_lookup(identity):
        return str(identity)

    migrate = Migrate(app, db)

    from routes.auth_routes import auth_bp
    from routes.project_routes import project_bp
    from routes.staff_routes import staff_bp
    from routes.task_routes import task_bp
    from routes.assignment_routes import assignment_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(project_bp)
    app.register_blueprint(staff_bp)
    app.register_blueprint(task_bp)
    app.register_blueprint(assignment_bp)

    # Регистрация глобального обработчика ошибок
    register_error_handlers(app)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
