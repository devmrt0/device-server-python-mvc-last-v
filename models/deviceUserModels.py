import json
import os
from app.utils.api_response import *


class DeviceUsers():

    def __init__(self):
        self.list = dict()
        self.filename = os.getcwd() + "/app/data/devices.json"

    def load(self):
        try:
            with open(self.filename) as json_file:
                json_data = json.load(json_file)
            for JsonObj in json_data:
                self.list[JsonObj.get('id')] = JsonObj
        except Exception as e:
            print(str(e))

    def authDevice(self, id, password):
        userFound = self.list.get(id)
        if userFound != None:
            return (userFound.get(password, '') == password)
        else:
            return False

    def hasDevice(self, id):
        with open(self.filename) as json_file:
            json_data = json.load(json_file)
        match = next((d for d in json_data if d['uid'] == id), 'false')
        return match

    def get(self):
        if len(self.list) == 0:
            return warning(10007)
        else:
            return success(list(self.list.values()))

    def getById(self, id):
        with open(self.filename) as json_file:
            json_data = json.load(json_file)
        if self.hasDevice(id) != 'false':
            return success(next((d for d in json_data if d['id'] == id), 'false'), "")
        else:
            return warning(10007, "")

    def postDevice(self, data):
        json_object = json.dumps(data, indent=14)
        with open(self.filename) as json_file:
            json_file.write(json_object)
        return success(json_object, "")

    def deleteDeviceById(self, id):
        with open(self.filename) as json_file:
            json_data = json.load(json_file)
        if self.hasDevice(id) != 'false':
            for idx, obj in enumerate(json_data):
                if obj['id'] == id:
                    json_data.pop(idx)
                    with open(self.filename, 'w', encoding='utf-8') as f:
                        f.write(json.dumps(json_data, indent=3))
                    break
                return success("", "")
        else:
            return warning(10007)

    def putUserById(self, id, data):
        post_data = data.get_json()
        id = post_data.get('id')
        name = post_data.get('name')
        password = post_data.get('password')

        with open(self.filename) as json_file:
            json_data = json.load(json_file)
        if self.hasDevice(id) != 'false':
            user = next((d for d in json_data if d['uid'] == id), 'false')
            if (id != None):
                user['id'] = id
            if (name != None):
                user['name'] = name
            if (password != None):
                user['password'] = password

            with open(self.filename, 'w') as fp:
                json.dump(json_data, fp, indent=5)
                return success(user, "")
        else:
            return warning(10007)


deviceUsers = DeviceUsers()
deviceUsers.load()
