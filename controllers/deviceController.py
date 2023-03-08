from flask import jsonify, request, make_response
from app.middleware.authJwt import Verifytoken
from app.utils.api_response import *
from app.models.deviceModels import devices


class DeviceController():

    @Verifytoken
    def getUserUniqueIdCommand(self,device_id,user_id):
     try:
        data = {'user_id': user_id}
        result = devices.addCommandToList('get',"user_uniqueid",device_id,None,data,None)
        if (result['status'] == None):
            return make_response(jsonify({'message': 'Server Error Undefined Error'}), 500)
        elif (result['status'] == -1) and (result['code'] == 10012 or result['code'] == 10013 or result['code'] == 10014 ):
            return make_response(jsonify({'result': result}), 400)
        else:
            return make_response(jsonify({'result': result}), 200)     
     except OSError as err:
         return make_response(jsonify({'message': 'Server Error'}), 500)

    @Verifytoken
    def postUserUniqueIdCommand(self,deviceid,user_id):
     try:
        post_data = request.get_json()
        post_data['user_id'] = user_id
        result = devices.addCommandToList('post',"user_uniqueid",deviceid,None,post_data,None)
        if (result['status'] == None):
            return make_response(jsonify({'message': 'Server Error Undefined Error'}), 500)
        elif (result['status'] == -1) and (result['code'] == 10012 or result['code'] == 10013 or result['code'] == 10014 ):
            return make_response(jsonify({'result': result}), 400)
        else:
            return make_response(jsonify({'result': result}), 200)     
     except OSError as err:
         return make_response(jsonify({'message': 'Server Error'}), 500)

    @Verifytoken
    def deleteUserUniqueIdCommand(self,deviceid,user_id):
     try:
        data = {'user_id': user_id}
        result = devices.addCommandToList('delete',"user_uniqueid_all",deviceid,None,data,None)
        if (result['status'] == None):
            return make_response(jsonify({'message': 'Server Error Undefined Error'}), 500)
        elif (result['status'] == -1) and (result['code'] == 10012 or result['code'] == 10013 or result['code'] == 10014 ):
            return make_response(jsonify({'result': result}), 400)
        else:
            return make_response(jsonify({'result': result}), 200)     
     except OSError as err:
         return make_response(jsonify({'message': 'Server Error'}), 500)

    @Verifytoken
    def deleteUserUniqueIdCommandById(self,deviceid,user_id,uniqueid):
      try:
        data = {'user_id': user_id, 'uniqueid':uniqueid}
        result = devices.addCommandToList('delete',"user_uniqueid_all",deviceid,None,data,None)
        if (result['status'] == None):
            return make_response(jsonify({'message': 'Server Error Undefined Error'}), 500)
        elif (result['status'] == -1) and (result['code'] == 10012 or result['code'] == 10013 or result['code'] == 10014 ):
            return make_response(jsonify({'result': result}), 400)
        else:
            return make_response(jsonify({'result': result}), 200)     
      except OSError as err:
         return make_response(jsonify({'message': 'Server Error'}), 500)

    @Verifytoken
    def getUserProfilePhotoCommand(self,deviceid,user_id):
     try:
        data = {'user_id': user_id}
        result = devices.addCommandToList('get',"user_photo_profile",deviceid,None,data,None)
        if (result['status'] == None):
            return make_response(jsonify({'message': 'Server Error Undefined Error'}), 500)
        elif (result['status'] == -1) and (result['code'] == 10012 or result['code'] == 10013 or result['code'] == 10014 ):
            return make_response(jsonify({'result': result}), 400)
        else:
            return make_response(jsonify({'result': result}), 200)     
     except OSError as err:
         return make_response(jsonify({'message': 'Server Error'}), 500)

    @Verifytoken
    def postUserProfilePhotoCommand(self,deviceid,user_id):
     try:
        post_data = request.get_json()
        post_data['user_id'] = user_id
        result = devices.addCommandToList('post',"user_photo_profile",deviceid,None,post_data,None)
        if (result['status'] == None):
            return make_response(jsonify({'message': 'Server Error Undefined Error'}), 500)
        elif (result['status'] == -1) and (result['code'] == 10012 or result['code'] == 10013 or result['code'] == 10014 ):
            return make_response(jsonify({'result': result}), 400)
        else:
            return make_response(jsonify({'result': result}), 200)     
     except OSError as err:
         return make_response(jsonify({'message': 'Server Error'}), 500)

    @Verifytoken
    def deleteUserProfilePhotoCommand(self,deviceid,user_id):
     try:
        data = {'user_id': user_id}
        result = devices.addCommandToList('delete',"user_photo_profile",deviceid,None,data,None)
        if (result['status'] == None):
            return make_response(jsonify({'message': 'Server Error Undefined Error'}), 500)
        elif (result['status'] == -1) and (result['code'] == 10012 or result['code'] == 10013 or result['code'] == 10014 ):
            return make_response(jsonify({'result': result}), 400)
        else:
            return make_response(jsonify({'result': result}), 200)     
     except OSError as err:
         return make_response(jsonify({'message': 'Server Error'}), 500)

    @Verifytoken
    def getUserTzCommandByDate(self,deviceid,user_id,date):
     try:
        data = {'user_id': user_id,'date':date}
        result = devices.addCommandToList('get',"user_time_zone",deviceid,None,data,None)
        if (result['status'] == None):
            return make_response(jsonify({'message': 'Server Error Undefined Error'}), 500)
        elif (result['status'] == -1) and (result['code'] == 10012 or result['code'] == 10013 or result['code'] == 10014 ):
            return make_response(jsonify({'result': result}), 400)
        else:
            return make_response(jsonify({'result': result}), 200)     
     except OSError as err:
         return make_response(jsonify({'message': 'Server Error'}), 500)

    @Verifytoken
    def postUserTzCommand(self,deviceid,user_id):
     try:
        data = {'user_id': user_id , 'date':'reg.params date url de belirtilmemiş'}
        result = devices.addCommandToList('get',"user_time_zone_all",deviceid,None,data,None)
        if (result['status'] == None):
            return make_response(jsonify({'message': 'Server Error Undefined Error'}), 500)
        elif (result['status'] == -1) and (result['code'] == 10012 or result['code'] == 10013 or result['code'] == 10014 ):
            return make_response(jsonify({'result': result}), 400)
        else:
            return make_response(jsonify({'result': result}), 200)     
     except OSError as err:
         return make_response(jsonify({'message': 'Server Error'}), 500)
     

    @Verifytoken
    def getUserTzCommand(self,deviceid,user_id):
     try:
        data = {'user_id': user_id , 'date':'reg.params date url de belirtilmemiş'}
        result = devices.addCommandToList('get',"user_time_zone_all",deviceid,None,data,None)
        if (result['status'] == None):
            return make_response(jsonify({'message': 'Server Error Undefined Error'}), 500)
        elif (result['status'] == -1) and (result['code'] == 10012 or result['code'] == 10013 or result['code'] == 10014 ):
            return make_response(jsonify({'result': result}), 400)
        else:
            return make_response(jsonify({'result': result}), 200)     
     except OSError as err:
         return make_response(jsonify({'message': 'Server Error'}), 500)

    @Verifytoken
    def deleteUserTzCommandByDate(self,deviceid,user_id,date):
     try:
        data = {'user_id': user_id,'date':date}
        result = devices.addCommandToList('delete',"user_time_zone",deviceid,None,data,None)
        if (result['status'] == None):
            return make_response(jsonify({'message': 'Server Error Undefined Error'}), 500)
        elif (result['status'] == -1) and (result['code'] == 10012 or result['code'] == 10013 or result['code'] == 10014 ):
            return make_response(jsonify({'result': result}), 400)
        else:
            return make_response(jsonify({'result': result}), 200)     
     except OSError as err:
         return make_response(jsonify({'message': 'Server Error'}), 500)

    @Verifytoken
    def deleteUserTzCommand(self,deviceid,user_id):
     try:
        data = {'user_id': user_id }
        result = devices.addCommandToList('delete',"user_time_zone_all",deviceid,None,data,None)
        if (result['status'] == None):
            return make_response(jsonify({'message': 'Server Error Undefined Error'}), 500)
        elif (result['status'] == -1) and (result['code'] == 10012 or result['code'] == 10013 or result['code'] == 10014 ):
            return make_response(jsonify({'result': result}), 400)
        else:
            return make_response(jsonify({'result': result}), 200)     
     except OSError as err:
         return make_response(jsonify({'message': 'Server Error'}), 500)

    @Verifytoken
    def getCommandCount(self,deviceid,command):
     try:
        result = devices.addCommandToList('get',command + "_count",deviceid,None,None,None)
        if (result['status'] == None):
            return make_response(jsonify({'message': 'Server Error Undefined Error'}), 500)
        elif (result['status'] == -1) and (result['code'] == 10012 or result['code'] == 10013 or result['code'] == 10014 ):
            return make_response(jsonify({'result': result}), 400)
        else:
            return make_response(jsonify({'result': result}), 200)     
     except OSError as err:
         return make_response(jsonify({'message': 'Server Error'}), 500)

    @Verifytoken
    def getCommandList(self,deviceid,command):
     try:
        result = devices.addCommandToList('get',command + "_list",deviceid,None,None,None)
        if (result['status'] == None):
            return make_response(jsonify({'message': 'Server Error Undefined Error'}), 500)
        elif (result['status'] == -1) and (result['code'] == 10012 or result['code'] == 10013 or result['code'] == 10014 ):
            return make_response(jsonify({'result': result}), 400)
        else:
            return make_response(jsonify({'result': result}), 200)     
     except OSError as err:
         return make_response(jsonify({'message': 'Server Error'}), 500)
    
    @Verifytoken
    def getCommand(self, deviceid, command):
        try:
            result = devices.addCommandToList(
                'get', command, deviceid, request.args, None, None)
            status = result.get('status', None)
            if status == None:
                return make_response(jsonify({'message': "Server Error. Undefinde Error"}), 500)
            elif (status == -1) and (result.get('code') in [10012, 10013, 10014]):
                return make_response(result, 400)
            else:
                return make_response(result, 200)
        except Exception as e:
            return make_response(jsonify({'message': "Server Error. " + str(e)}), 500)

    @Verifytoken
    def getCommandByid(self, deviceid, command,id):
     try:
        result = devices.addCommandToList('get',command,deviceid,"",None,id)
        if (result['status'] == None):
            return make_response(jsonify({'message': 'Server Error Undefined Error'}), 500)
        elif (result['status'] == -1) and (result['code'] == 10012 or result['code'] == 10013 or result['code'] == 10014 ):
            return make_response(jsonify({'result': result}), 400)
        else:
            return make_response(jsonify({'result': result}), 200)     
     except:
         return make_response(jsonify({'message': 'Server Error'}), 500)

    @Verifytoken
    def postCommand(self, deviceid, command):
     try:
        post_data = request.get_json()
        result = devices.addCommandToList('post',command,deviceid,None,post_data,None)
        if (result['status'] == None):
            return make_response(jsonify({'message': 'Server Error Undefined Error'}), 500)
        elif (result['status'] == -1) and (result['code'] == 10012 or result['code'] == 10013 or result['code'] == 10014 ):
            return make_response(jsonify({'result': result}), 400)
        else:
            return make_response(jsonify({'result': result}), 200)     
     except OSError as err:
         return make_response(jsonify({'message': 'Server Error'}), 500) 

    @Verifytoken
    def postCommandByid(self, deviceid, command,id):
     try:
        post_data = request.get_json()
        result = devices.addCommandToList('post',command,deviceid,None,post_data,id)
        if (result['status'] == None):
            return make_response(jsonify({'message': 'Server Error Undefined Error'}), 500)
        elif (result['status'] == -1) and (result['code'] == 10012 or result['code'] == 10013 or result['code'] == 10014 ):
            return make_response(jsonify({'result': result}), 400)
        else:
            return make_response(jsonify({'result': result}), 200)     
     except:
         return make_response(jsonify({'message': 'Server Error'}), 500)

    @Verifytoken
    def deleteCommand(self, deviceid, command):
     try:
        result = devices.addCommandToList('delete',command,deviceid,None,None,None)
        if (result['status'] == None):
            return make_response(jsonify({'message': 'Server Error Undefined Error'}), 500)
        elif (result['status'] == -1) and (result['code'] == 10012 or result['code'] == 10013 or result['code'] == 10014 ):
            return make_response(jsonify({'result': result}), 400)
        else:
            return make_response(jsonify({'result': result}), 200)     
     except OSError as err:
         return make_response(jsonify({'message': 'Server Error'}), 500)

    @Verifytoken
    def deleteCommandByid(self, deviceid, command,id):
     try:
        result = devices.addCommandToList('delete',command,deviceid,"",None,id)
        if (result['status'] == None):
            return make_response(jsonify({'message': 'Server Error Undefined Error'}), 500)
        elif (result['status'] == -1) and (result['code'] == 10012 or result['code'] == 10013 or result['code'] == 10014 ):
            return make_response(jsonify({'result': result}), 400)
        else:
            return make_response(jsonify({'result': result}), 200)     
     except:
         return make_response(jsonify({'message': 'Server Error'}), 500)
        

deviceController = DeviceController()
