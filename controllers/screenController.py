from flask import jsonify, request, make_response
from app.middleware.authJwt import Verifytoken
from app.utils.api_response import *
from app.models.screenModels import screens


class ScreenController():

    @Verifytoken
    def getScreenAll(self):
        try:
           return make_response(jsonify(screens.getAll()), 200)
        except:
          return make_response(jsonify({'message': 'Server Error'}), 500)

    @Verifytoken
    def getScreenById(self, id):
        try:
           return make_response(jsonify(screens.getById(id)), 200)
        except:
          return make_response(jsonify({'message': 'Server Error'}), 500)

    @Verifytoken
    def putScreenById(self, id):
        post_data = request.get_json()
        try:
           return make_response(jsonify(screens.putScreenById(id,post_data)), 200)
        except:
           return make_response(jsonify({'message': 'Server Error'}), 500)


screenController = ScreenController()
