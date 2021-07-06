from Parser import *
import Enum
from Room import *

class DataAnalyzer:
    def __init__(self):
        print("DataAnalyzer initialized")

    def getRoomsArray(self):
        print("Parsing room list...")
        rooms = []
        for i in range(1, Enum.ROOM_COUNT + 1):
            room = parser.getRoom(i)
            parsed = jsonParser.parseRoom(room)
            rooms.append(room)
        print("Room list parsed")
        return rooms

dataAnalyzer = DataAnalyzer()
Enum.ROOMS = dataAnalyzer.getRoomsArray()