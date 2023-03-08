from flask import jsonify, request, make_response
from app.utils.common import isEmpty
from app.models.deviceUserModels import DeviceUsers
from app.middleware.authJwt import Verifytoken
from app.utils.api_response import *


class DeviceUserController(DeviceUsers):

    def __init__(self):
        super().__init__()

    @Verifytoken
    def getDeviceAll(self):
        try:
            return make_response(self.get(), 200)
        except Exception as e:
            return make_response(jsonify({'message': "Server Error. " + str(e)}), 500)
    @Verifytoken
    def getDeviceById(self,id):
        try:
            return make_response(DeviceUsers.getById(id), 200)
        except Exception as e:
            return make_response(jsonify({'message': "Server Error. " + str(e)}), 500)
    @Verifytoken
    def putDeviceById(self,id):
        post_data = request.get_json()
        try:
           return make_response(jsonify(DeviceUsers.putUserById(id,post_data)), 200)
        except:
           return make_response(jsonify({'message': 'Server Error'}), 500)
    @Verifytoken
    def postDevice(self):
        post_data = request.get_json()
        try:
           return make_response(jsonify(DeviceUsers.postDevice(post_data)), 200)
        except:
           return make_response(jsonify({'message': 'Server Error'}), 500)
    @Verifytoken
    def deleteDeviceById(self,id):
        try:
           return make_response(jsonify(DeviceUsers.deleteDeviceById(id)), 200)
        except:
           return make_response(jsonify({'message': 'Server Error'}), 500)

deviceUserController = DeviceUserController()
deviceUserController.load()
