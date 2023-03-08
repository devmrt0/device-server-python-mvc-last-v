from flask import Blueprint
from app.controllers.eventController import eventController

event_api = Blueprint('event_api', __name__, url_prefix='/api')

event_api.add_url_rule('/event/door/open',
                        view_func=eventController.doorOpen, methods=['POST'])

event_api.add_url_rule('/event/alarm/door/open',
                        view_func=eventController.doorOpenAlarm, methods=['POST'])

event_api.add_url_rule('/event/alarm/door/close',
                        view_func=eventController.doorCloseAlarm, methods=['POST'])

