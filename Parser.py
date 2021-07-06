import requests
import Room
import json
import Enum

class Parser:
    def __init__(self):
        print("Parser initialized")

    def getRoom(self, id):
        response = requests.get(Enum.SITE_URL + str(id)).json()
        return response

class JSONParser:
    def __init__(self):
        print("JSONParser initialized")
    
    #Парсинг устройства
    def parseMeasurement(self, json_responce):
        propertyName = json_responce["property"]
        value = json_responce["value"]
        state = json_responce["state"]

        return Room.Measurment(propertyName, value, state)
    
    #Парсинг комнат
    def parseRoom(self, json_responce):
        deviceId = json_responce[0]['deviceId']
        room = json_responce[0]['room']
        measurements = []
        for i in range(Enum.DEVICE_COUNT):
            to_append = self.parseMeasurement(json_responce[0]['measurements'][i])
            measurements.append(to_append)

        return Room.Room(deviceId, room, measurements)
    
    #Парсинг локализации
    def parseLocale(self, locale_file_name):
        result = ""
        with open(locale_file_name) as f:
            result = json.load(f)
        print("Locale parsed")
        Enum.LOCALE = result

jsonParser = JSONParser()
jsonParser.parseLocale(Enum.LOCALE_FILE_NAME)
parser = Parser()

if __name__ == '__main__':
    json_string = parser.getRoom(1)
    print(json_string)
    print("\n--++--\n")
    parsed = jsonParser.parseRoom(json_string)
    print(parsed.getString())