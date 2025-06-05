from flask_smorest import Blueprint, abort
from flask.views import MethodView
from flask_jwt_extended import jwt_required
from marshmallow import Schema, fields


from services.staff_service import (
    create_staff, get_all_staff, add_xp_to_staff, assign_skill_upgrade,
    add_fatigue_to_staff, rest_staff, get_effective_speed, trigger_random_event
)

blp = Blueprint('staff', 'staff', url_prefix='/api/staff', description='Staff operations')

class StaffSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    role = fields.Str(required=True)
    speed = fields.Float(required=True)
    cost = fields.Float(required=True)

class XPUpdateSchema(Schema):
    xp_amount = fields.Int(required=True)

class SkillUpdateSchema(Schema):
    skill = fields.Str(required=True)

class FatigueUpdateSchema(Schema):
    fatigue_amount = fields.Int(required=True)

@blp.route('/')
class StaffList(MethodView):
    @jwt_required()
    @blp.response(200, StaffSchema(many=True))
    def get(self):
        """Получение всех сотрудников"""
        return get_all_staff()

    @jwt_required()
    @blp.arguments(StaffSchema)
    @blp.response(201, StaffSchema)
    def post(self, staff_data):
        """Создание нового сотрудника"""
        response, status = create_staff(**staff_data)
        return response

@blp.route('/<int:staff_id>/add_xp')
class StaffXP(MethodView):
    @jwt_required()
    @blp.arguments(XPUpdateSchema)
    def post(self, xp_data, staff_id):
        """Добавить опыт сотруднику"""
        response, status = add_xp_to_staff(staff_id, xp_data['xp_amount'])
        return response, status

@blp.route('/<int:staff_id>/assign_skill')
class StaffSkill(MethodView):
    @jwt_required()
    @blp.arguments(SkillUpdateSchema)
    def post(self, skill_data, staff_id):
        """Назначить новый навык сотруднику"""
        response, status = assign_skill_upgrade(staff_id, skill_data['skill'])
        return response, status

@blp.route('/<int:staff_id>/add_fatigue')
class StaffFatigue(MethodView):
    @jwt_required()
    @blp.arguments(FatigueUpdateSchema)
    def post(self, fatigue_data, staff_id):
        """Добавить усталость сотруднику"""
        response, status = add_fatigue_to_staff(staff_id, fatigue_data['fatigue_amount'])
        return response, status

@blp.route('/<int:staff_id>/rest')
class StaffRest(MethodView):
    @jwt_required()
    def post(self, staff_id):
        """Отправить сотрудника на отдых"""
        response, status = rest_staff(staff_id)
        return response, status

@blp.route('/<int:staff_id>/effective_speed')
class StaffEffectiveSpeed(MethodView):
    @jwt_required()
    def get(self, staff_id):
        """Получить эффективную скорость сотрудника"""
        response, status = get_effective_speed(staff_id)
        return response, status

@blp.route('/<int:staff_id>/random_event')
class StaffRandomEvent(MethodView):
    @jwt_required()
    def post(self, staff_id):
        """Сгенерировать случайное событие для сотрудника"""
        response, status = trigger_random_event(staff_id)
        return response, status
