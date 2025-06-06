from flask_smorest import Blueprint, abort
from flask.views import MethodView
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import Schema, fields
from models.project import Project
from extensions import db

blp = Blueprint('projects', 'projects', url_prefix='/api/projects', description='Project operations')

class ProjectSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    budget = fields.Int(required=True)
    user_id = fields.Int(dump_only=True)

class ProjectCreateSchema(Schema):
    name = fields.Str(required=True)
    budget = fields.Int(required=True)

@blp.route('/')
class ProjectsList(MethodView):
    @jwt_required()
    @blp.response(200, ProjectSchema(many=True))
    def get(self):
        """Получение только проектов текущего пользователя"""
        user_id = get_jwt_identity()
        projects = Project.query.filter_by(user_id=user_id).all()
        return projects

    @jwt_required()
    @blp.arguments(ProjectCreateSchema)
    @blp.response(201, ProjectSchema)
    def post(self, project_data):
        """Создание нового проекта"""
        user_id = get_jwt_identity()
        project = Project(name=project_data['name'], budget=project_data['budget'], user_id=user_id)
        db.session.add(project)
        db.session.commit()
        return project
 
 