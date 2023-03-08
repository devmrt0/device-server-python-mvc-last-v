from flask import jsonify, request, make_response
from app.middleware.authJwt import Verifytoken
from app.utils.api_response import *
from app.models.eventModels import deviceEvents


class EventController():

    @Verifytoken
    def doorOpen(self):
        post_data = request.get_json()
        uid = post_data.get('device_dt')
        deviceid = post_data.get('deviceid')
        language = post_data.get('language')
        try:
            return make_response(jsonify(deviceEvents.doorOpen(deviceid, language, uid)), 200)
        except:
            return make_response(jsonify({'message': 'Server Error'}), 500)

    @Verifytoken
    def doorOpenAlarm(self):
        post_data = request.get_json()
        uid = post_data.get('device_dt')
        deviceid = post_data.get('deviceid')
        language = post_data.get('language')
        try:
            return make_response(jsonify(deviceEvents.doorAlarmOpen(deviceid, language, uid)), 200)
        except:
            return make_response(jsonify({'message': 'Server Error'}), 500)

    @Verifytoken
    def doorCloseAlarm(self, id):
        post_data = request.get_json()
        uid = post_data.get('device_dt')
        deviceid = post_data.get('deviceid')
        language = post_data.get('language')
        try:
            return make_response(jsonify(deviceEvents.doorAlarmClose(deviceid, language, uid)), 200)
        except:
            return make_response(jsonify({'message': 'Server Error'}), 500)

eventController = EventController()

