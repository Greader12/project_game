from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from config import Config
import os
from flasgger import Swagger  # <-- подключаем Flasgger
from models import user, project, task, staff, assignment, event
from models import db  # импортируем `db` из models

basedir = os.path.abspath(os.path.dirname(__file__))

jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)

    # 👇 Инициализация Swagger
    Swagger(app)

    # 👇 Гарантируем, что identity в JWT будет строкой
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

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
