from flask import jsonify, request, make_response
from app.middleware.authJwt import Verifytoken
from app.utils.api_response import *
from app.models.verifyModels import users


class VerifyController():

    @Verifytoken
    def verifyUid(self):
        post_data = request.get_json()
        uid = post_data.get('uid')
        deviceid = post_data.get('deviceid')
        language = post_data.get('language')
        try:
            return make_response(jsonify(users.verifyUid(deviceid, uid, language)), 200)
        except:
            return make_response(jsonify({'message': 'Server Error'}), 500)

    @Verifytoken
    def verifyBio(self):
       post_data = request.get_json()
       uid = post_data.get('uid')
       deviceid = post_data.get('deviceid')
       language = post_data.get('language') 
       try:
          return make_response(jsonify(users.verifyFace(deviceid,uid,language)), 200)
       except:
          return make_response(jsonify({'message': 'Server Error'}), 500)

    @Verifytoken
    def verifyQR(self):
        post_data = request.get_json()
        uid = post_data.get('uid')
        deviceid = post_data.get('deviceid')
        language = post_data.get('language') 
        try:
           return make_response(jsonify(users.verifyQR(deviceid,uid,language)), 200)
        except:
           return make_response(jsonify({'message': 'Server Error'}), 500)

    @Verifytoken
    def getUserAll(self):
        try:
           return make_response(jsonify(users.getAll()), 200)
        except:
           return make_response(jsonify({'message': 'Server Error'}), 500)

    @Verifytoken
    def getUserById(self, id):
        try:
           return make_response(jsonify(users.getById(id)), 200)
        except:
           return make_response(jsonify({'message': 'Server Error'}), 500)

    @Verifytoken
    def putUserById(self, id):
        post_data = request.get_json()
        try:
           return make_response(jsonify(users.putUserById(id,post_data)), 200)
        except:
           return make_response(jsonify({'message': 'Server Error'}), 500)

    @Verifytoken
    def postUser(self):
        post_data = request.get_json()
        try:
           return make_response(jsonify(users.postUser(post_data)), 200)
        except:
           return make_response(jsonify({'message': 'Server Error'}), 500)

    @Verifytoken
    def deleteUserById(self, id):
        try:
           return make_response(jsonify(users.deleteUserById(id)), 200)
        except:
           return make_response(jsonify({'message': 'Server Error'}), 500)


verifyController = VerifyController()
