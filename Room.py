import Parser
import Enum

#Комната
class Room:
    def __init__(self, deviceId, name, measurements):
        self.name = name
        self.deviceId = deviceId
        self.measurements = measurements

#Датчик
class Measurment:
    def __init__(self, propertyName, value, state):
        self.propertyName = propertyName,
        self.value = value
        self.state = state