import json
import os
from app.utils.api_response import *


class Screens():

    def __init__(self):
        self.list = dict()
        self.filename = os.getcwd() + "/app/data/screen.json"

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

    def hasScreen(self, id):
        with open(self.filename) as json_file:
            json_data = json.load(json_file)
        match = next((d for d in json_data if d['id'] == id), 'false')
        return match

    def getById(self, id):
        with open(self.filename) as json_file:
            json_data = json.load(json_file)
        if self.hasScreen(id) != 'false':
            return success(next((d for d in json_data if d['id'] == id), 'false'), "")
        else:
            return warning(10007, "")

    def getAll(self):
        with open(self.filename) as json_file:
            json_data = json.load(json_file)
        if len(json_data) == 0:
            return warning(10007, "")
        else:
            return success(json_data, "")

    def putScreenById(self, id, data):
        post_data = data.get_json()
        screen_type = post_data.get('screen_type')
        default_screen_type = post_data.get('default_screen_type')
        line_1 = post_data.get('line_1')
        line_2 = post_data.get('line_2')
        line_3 = post_data.get('line_3')
        footer = post_data.get('footer')
        screen_duration = post_data.get('screen_duration')
        infinite = post_data.get('infinite')
        tr_out_1_duration = post_data.get('tr_out_1_duration')
        tr_out_2_duration = post_data.get('tr_out_2_duration')
        rl_1_duration = post_data.get('rl_1_duration')
        rl_2_duration = post_data.get('rl_2_duration')
        sound_duration = post_data.get('sound_duration')
        with open(self.filename) as json_file:
            json_data = json.load(json_file)
        if self.hasScreen(id) != 'false':
            user = next((d for d in json_data if d['id'] == id), 'false')
            if (screen_type != None):
                user['screen_type'] = screen_type
            if (default_screen_type != None):
                user['default_screen_type'] = default_screen_type
            if (line_1 != None):
                user['line_1'] = line_1
            if (line_2 != None):
                user['line_2'] = line_2
            if (line_3 != None):
                user['line_3'] = line_3    
            if (footer != None):
                user['footer'] = footer
            if (screen_duration != None):
                user['screen_duration'] = screen_duration
            if (infinite != None):
                user['infinite'] = infinite 
            if (tr_out_1_duration != None):
                user['tr_out_1_duration'] = tr_out_1_duration
            if (tr_out_2_duration != None):
                user['tr_out_2_duration'] = tr_out_2_duration 
            if (rl_1_duration != None):
                user['rl_1_duration'] = rl_1_duration
            if (rl_2_duration != None):
                user['rl_2_duration'] = rl_2_duration 
            if (sound_duration != None):
                user['sound_duration'] = sound_duration                   
            with open(self.filename, 'w') as fp:
                json.dump(json_data, fp, indent=5)
                return success(user, "")
        else:
            return warning(10007)


screens = Screens()
screens.load()
