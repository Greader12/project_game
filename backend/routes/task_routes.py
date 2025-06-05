from flask_smorest import Blueprint, abort
from flask.views import MethodView
from flask_jwt_extended import jwt_required
from marshmallow import Schema, fields
from models.task import Task
from models import db

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
        """Получение списка задач"""
        tasks = Task.query.all()
        return tasks

    @jwt_required()
    @blp.arguments(TaskSchema)
    @blp.response(201, TaskSchema)
    def post(self, task_data):
        """Создание новой задачи"""
        task = Task(**task_data)
        db.session.add(task)
        db.session.commit()
        return task
