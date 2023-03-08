import json
import os
from app.utils.api_response import *


class Users():

    def __init__(self):
        self.list = dict()
        self.filename = os.getcwd() + "/app/data/whitelist.json"

    def load(self):
        try:
            with open(self.filename) as json_file:
                json_data = json.load(json_file)
            for JsonObj in json_data:
                self.add(JsonObj)
        except Exception as e:
            print(str(e))

    def add(self, command):
        url = command.get('url').strip()
        http_method = command.get('http_method').strip()
        method_type = command.get('method_type').strip()
        key = url + '_' + http_method + '_' + method_type
        self.list[key] = command

    def hasUser(self, id):
        with open(self.filename) as json_file:
            json_data = json.load(json_file)
        match = next((d for d in json_data if d['uid'] == id), 'false')
        return match

    def getAll(self):
        with open(self.filename) as json_file:
            json_data = json.load(json_file)
        if len(json_data) != 0:
            return success(json_data, "")
        else:
            return warning(10007, "")

    def getById(self, id):
        with open(self.filename) as json_file:
            json_data = json.load(json_file)
        if self.hasUser(id) != 'false':
            return success(next((d for d in json_data if d['id'] == id), 'false'), "")
        else:
            return warning(10007, "")

    def verifyUid(self, deviceid, uid, language):
        with open(self.filename) as json_file:
            json_data = json.load(json_file)
        if self.hasUser(uid) != 'false':
            screen = self.getById(1)
            del screen['data']['id']
            del screen['data']['default_screen_type']
            user = next((d for d in json_data if d['uid'] == uid), 'false')
            screen['data']['line_1']['text'] = user['name']
            screen['data']['line_3']['text'] = user['position']
            return screen
        else:
            screen = self.getById(2)
            return screen

    def verifyFace(deviceid, uid, language):
        return "In Development(Geliştirlecek)"

    def verifyQR(deviceid, uid, language):
        return "In Development(Geliştirlecek)"

    def postUser(self, data):
        json_object = json.dumps(data, indent=14)
        with open(self.filename) as json_file:
            json_file.write(json_object)
        return success(json_object, "")

    def deleteUserById(self, id):
        with open(self.filename) as json_file:
            json_data = json.load(json_file)
        if self.hasUser(id) != 'false':
            for idx, obj in enumerate(json_data):
                if obj['id'] == id:
                    json_data.pop(idx)
                    with open(self.filename, 'w', encoding='utf-8') as f:
                        f.write(json.dumps(json_data, indent=22))
                    break
                return success("", "")
        else:
            return warning(10007)

    def putUserById(self, id, data):
        post_data = data.get_json()
        uid = post_data.get('uid')
        name = post_data.get('name')
        position = post_data.get('position')
        photo = post_data.get('photo')
        access_enabled = post_data.get('access_enabled')
        with open(self.filename) as json_file:
            json_data = json.load(json_file)
        if self.hasUser(id) != 'false': 
           user = next((d for d in json_data if d['uid'] == id), 'false')
           if(uid != None):
            user['uid'] = uid
           if(name != None):
            user['name'] = name
           if(position != None):
            user['position'] = position 
           if(photo != None):
            user['photo'] = photo
           if(access_enabled != None):
            user['access_enabled'] = access_enabled
           with open(self.filename, 'w') as fp:
            json.dump(json_data, fp, indent=5) 
            return success(user, "")
        else:
            return warning(10007)   


users = Users()
users.load()
