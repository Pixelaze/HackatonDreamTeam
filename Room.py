import Parser
import Enum

#Комната
class Room:
    def __init__(self, deviceId, name, measurements):
        self.name = name
        self.deviceId = deviceId
        self.measurements = measurements

    def getString(self):
        string = Enum.LOCALE['room_print_schema_parents'].replace("%NAME%", self.name)
        return string

#Устройство
class Measurment:
    def __init__(self, propertyName, value, state):
        self.propertyName = propertyName,
        self.value = value
        self.state = state