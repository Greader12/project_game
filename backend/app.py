from flask import Flask
from flask_smorest import Api
from config import Config
from extensions import db, jwt
from models import gamesave
from flask_migrate import Migrate
from routes.auth_routes import blp as AuthBlueprint
from routes.project_routes import blp as ProjectBlueprint
from routes.staff_routes import blp as StaffBlueprint
from routes.task_routes import blp as TaskBlueprint
from routes.assignment_routes import blp as AssignmentBlueprint
from routes.token_routes import blp as TokenBlueprint
from routes.event_routes import blp as EventBlueprint
from routes.admin_task_routes import blp as AdminTaskBlueprint
from utils.error_handlers import register_error_handlers  # если есть кастомные обработчики ошибок
from flask_cors import CORS
from routes.save import blp as SaveBlueprint

def create_app():
    app = Flask(__name__)

    # ✅ Конфигурация API ДО создания Api
    app.config['API_TITLE'] = 'Project Management Game API'
    app.config['API_VERSION'] = '1.0.0'
    app.config['OPENAPI_VERSION'] = '3.0.3'
    app.config['OPENAPI_URL_PREFIX'] = '/api/docs'
    app.config['OPENAPI_SWAGGER_UI_PATH'] = '/'
    app.config['OPENAPI_SWAGGER_UI_URL'] = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'

    app.config.from_object(Config)

    # ✅ Настройка CORS
    CORS(app, resources={r"/api/*": {"origins": ["http://localhost:3000", "http://localhost:5173"]}}, supports_credentials=True)

    # ✅ Инициализация расширений
    db.init_app(app)
    jwt.init_app(app)

    # ✅ Создание API
    api = Api(app, spec_kwargs={
        "security": [{"BearerAuth": []}],
        "components": {
            "securitySchemes": {
                "BearerAuth": {
                    "type": "http",
                    "scheme": "bearer",
                    "bearerFormat": "JWT",
                }
            }
        },
    })

    # ✅ Регистрация всех блюпринтов
    api.register_blueprint(AuthBlueprint)
    api.register_blueprint(ProjectBlueprint)
    api.register_blueprint(StaffBlueprint)
    api.register_blueprint(TaskBlueprint)
    api.register_blueprint(AssignmentBlueprint)
    api.register_blueprint(TokenBlueprint)
    api.register_blueprint(EventBlueprint)
    api.register_blueprint(AdminTaskBlueprint)
    api.register_blueprint(SaveBlueprint)

    # ✅ Настройка JWT Identity
    @jwt.user_identity_loader
    def user_identity_lookup(identity):
        return str(identity)

    # ✅ Настройка миграций
    migrate = Migrate(app, db)

    # ✅ Регистрация обработчиков ошибок
    register_error_handlers(app)

    return app

# Создание приложения
app = create_app()

if __name__ == "__main__":
    # Для локальной разработки удобно слушать на всех интерфейсах
    app.run(debug=True, host="0.0.0.0", port=5000)
