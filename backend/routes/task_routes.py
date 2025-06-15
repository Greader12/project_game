from flask_smorest import Blueprint, abort
from flask.views import MethodView
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import Schema, fields
from models.task import Task
from models.project import Project
from extensions import db
from utils.permissions import admin_required
from services import task_service  # обязательно подключи task_service

blp = Blueprint('tasks', 'tasks', url_prefix='/api/tasks', description='Task operations')


class TaskSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    base_duration = fields.Int(required=True)
    base_cost = fields.Int(required=True)
    project_id = fields.Int(required=True)
    start_week = fields.Int(required=True)


@blp.route('/')
class TasksList(MethodView):
    @jwt_required()
    @blp.response(200, TaskSchema(many=True))
    def get(self):
        """Получение задач пользователя"""
        user_id = get_jwt_identity()
        user_project_ids = [p.id for p in Project.query.filter_by(user_id=user_id).all()]
        tasks = Task.query.filter(Task.project_id.in_(user_project_ids)).all()
        return tasks

    @jwt_required()
    @admin_required
    @blp.arguments(TaskSchema)
    @blp.response(201, TaskSchema)
    def post(self, task_data):
        """Создание новой задачи"""
        task = Task(**task_data)
        db.session.add(task)
        db.session.commit()
        return task


@blp.route("/simulate_week", methods=["POST"])
@jwt_required()
def simulate_week():
    """Симуляция недели: продвижение задач"""
    user_id = get_jwt_identity()
    return task_service.simulate_week(user_id)
