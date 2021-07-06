import Parser
import Enum

#Комната
class Room:
    def __init__(self, deviceId, name, devices):
        self.name = name
        self.deviceId = deviceId
        self.devices = devices

    def getString(self):
        

#Устройство
class Measurment:
    def __init__(self, propertyName, value, state):
        self.propertyName = propertyName,
        self.value = value
        self.state = state
    
    def getString(self):
        pass

def getStringRoom(room_id):
    string = Enum.LOCALE['room_print_schema_parents'].replace("%NAME%", self.name)
    return string

def getStringDevices(room_id)