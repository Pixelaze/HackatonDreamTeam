import requests
import Room
import json

class Parser:
    def __init__(self):
        print("Parser initialized")

    #TODO

class JSONParser:
    def __init__(self):
        print("JSONParser initialized")
    
    #Парсинг устройства
    def parseMeasurement(self, json_string):
        json_string = json.loads(json_string)

        propertyName = json_string["property"]
        value = json_string["value"]
        state = json_string["state"]

        return Room.Measurment(propertyName, value, state)
    
    #Парсинг комнат
    def parseRoom(self, json_string):
        json_string = json.loads(json_string)

        deviceId = json_string["deviceId"]
        room = json_string["room"]
        measurements = []
        for i in range(9):
            measurements.append(parseMeasurement(json_string["measurements"][i]))

        return Room.Room(deviceId, room, measurements)

parser = Parser()