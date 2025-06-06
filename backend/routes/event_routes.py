from flask.views import MethodView
from flask_smorest import Blueprint
from flask_jwt_extended import jwt_required
from models.event import Event
from marshmallow import Schema, fields

blp = Blueprint('events', __name__, url_prefix='/api/events', description='Event log')

class EventSchema(Schema):
    id = fields.Int()
    staff_id = fields.Int()
    project_id = fields.Int()
    type = fields.Str()
    week = fields.Int()

@blp.route('/')
class EventList(MethodView):
    @jwt_required()
    @blp.response(200, EventSchema(many=True))
    def get(self):
        """Получить все события"""
        events = Event.query.all()
        return events
