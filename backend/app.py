from flask import Flask
from flask_smorest import Api
from config import Config
from extensions import db, jwt
from flask_migrate import Migrate
from routes.auth_routes import blp as AuthBlueprint
from routes.project_routes import blp as ProjectBlueprint
from routes.staff_routes import blp as StaffBlueprint
from routes.task_routes import blp as TaskBlueprint
from routes.assignment_routes import blp as AssignmentBlueprint
from utils.error_handlers import register_error_handlers  # если у тебя есть кастомные обработчики ошибок
from extensions import db, jwt
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # ✅ Конфигурация API ДО создания Api
    app.config['API_TITLE'] = 'Project Management Game API'
    app.config['API_VERSION'] = '1.0.0'
    app.config['OPENAPI_VERSION'] = '3.0.3'
    app.config['OPENAPI_URL_PREFIX'] = '/api/docs'
    app.config['OPENAPI_SWAGGER_UI_PATH'] = '/'
    app.config['OPENAPI_SWAGGER_UI_URL'] = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'

    db.init_app(app)
    jwt.init_app(app)

    # ✅ Создаём API уже после конфигурации
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

    # Регистрация блюпринтов
    api.register_blueprint(AuthBlueprint)
    api.register_blueprint(ProjectBlueprint)
    api.register_blueprint(StaffBlueprint)
    api.register_blueprint(TaskBlueprint)
    api.register_blueprint(AssignmentBlueprint)

    # Дополнительная настройка jwt (если требуется)
    @jwt.user_identity_loader
    def user_identity_lookup(identity):
        return str(identity)

    # Миграции
    migrate = Migrate(app, db)

    # Регистрация обработчиков ошибок
    register_error_handlers(app)

    return app



app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
