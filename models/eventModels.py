import json
import os
import uuid
from app.utils.api_response import *
from app.utils.common import isEmpty, JSONstringify
from app.utils.json_schema import SchemaValidate
import time

class DeviceEvent():

    def __init__(self, device_id, eventType, eventDate ):
        self.device_id = device_id
        self.eventType = eventType
        self.eventDate = eventDate

class DeviceEvents():

    def __init__(self):
        self.list = dict()
    
    def doorOpen(self,deviceid, language, device_dt):
        de = DeviceEvent(deviceid, language, device_dt)
        self.list[0] = de
        return success("","")
    
    def doorAlarmOpen(self,deviceid, language, device_dt):
        de = DeviceEvent(deviceid, language, device_dt)
        self.list[0] = de
        return success("","")
    
    def doorAlarmClose(self,deviceid, language, device_dt):
        de = DeviceEvent(deviceid, language, device_dt)
        self.list[0] = de
        return success("","")



deviceEvents = DeviceEvents()
deviceEvents.load()
       