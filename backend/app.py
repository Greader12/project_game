from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
import os

from models import db  # импортируем `db` из models

basedir = os.path.abspath(os.path.dirname(__file__))

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'instance', 'app.db')
    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['JWT_SECRET_KEY'] = 'your-jwt-secret-key'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)  # инициализируем тут, ПОСЛЕ создания app

    jwt = JWTManager(app)
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

app = create_app()  # создаём приложение тут!

if __name__ == "__main__":
    app.run(debug=True)
