import Parser
import Enum

#Комната
class Room:
    def __init__(self, deviceId, name, devices):
        self.name = name
        self.deviceId = deviceId
        self.devices = devices

    def getString(self):
        pass

#Устройство
class Measurment:
    def __init__(self, propertyName, value, state):
        self.propertyName = propertyName,
        self.value = value
        self.state = state
    
    def getString(self):
        pass

def getStringRoom(room_id):
    room = Enum.ROOMS[room_id][0]
    print(room)
    string = Enum.LOCALE['room_print_schema_parents'].replace("%NAME%", room["room"]).replace("%ID%", str(room_id))
    string += "\n" + getStringDevices(room_id, room)
    return string

def getStringDevices(room_id, room):
    schema = Enum.LOCALE['device_print_schema_parents']
    string = ""
    for i in range(Enum.DEVICE_COUNT):
        printing = schema.replace("%PROPERTY%", Enum.LOCALE[room['measurements'][i]['property']])
        if(type(room['measurements'][i]['value']) == float):
            value = round(room['measurements'][i]['value'], 3)
        else:
            value = room['measurements'][i]['value']
        printing = printing.replace("%VALUE%", str(value)) + "\n"
        string += printing
    return string