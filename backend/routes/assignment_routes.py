from flask_smorest import Blueprint, abort
from flask.views import MethodView
from flask_jwt_extended import jwt_required
from marshmallow import Schema, fields
from models.assignment import Assignment
from extensions import db

blp = Blueprint('assignments', 'assignments', url_prefix='/api/assignments', description='Assignment operations')

class AssignmentSchema(Schema):
    id = fields.Int(dump_only=True)
    task_id = fields.Int(required=True)
    staff_id = fields.Int(required=True)

@blp.route('/')
class AssignmentList(MethodView):
    @jwt_required()
    @blp.response(200, AssignmentSchema(many=True))
    def get(self):
        """Получение списка назначений"""
        assignments = Assignment.query.all()
        return assignments

    @jwt_required()
    @blp.arguments(AssignmentSchema)
    @blp.response(201, AssignmentSchema)
    def post(self, assignment_data):
        """Назначение сотрудника на задачу"""
        assignment = Assignment(**assignment_data)
        db.session.add(assignment)
        db.session.commit()
        return assignment
