from Model import Model
from models.Meeting import Meeting
from services.RoomService import RoomService
from services.DatabaseService import DatabaseService


class Room(Model):
    __tablename__ = 'room'
    __table_args__ = {'autoload': True, 'autoload_with': DatabaseService.DBEngine()}
    service = RoomService()

    @staticmethod
    def getById(room_id):
        room = Room.service.get(room_id)
        return room

    @staticmethod
    def getAvailableRooms(start, end):
        meetings = Meeting.getByTime(str(start), str(end))
        room_ids = list()
        for meet in meetings:
            room_ids.append(meet.room_id)
            print("r_id:" + room_id)
        rooms = None
        if (len(room_ids) > 0):
            rooms = Room.service.getAllByFilter(room_ids)
        else:
            rooms = Room.service.getAll()
        return rooms

    @staticmethod
    def getAll():
        room = Room.service.getAll()
        return room

    @staticmethod
    def getByName(name):
        room = Room.service.getByName(name)
        return room

    @staticmethod
    def add(room):
        old_admin = Room.service.getByName(room.name)
        if (old_admin is not None):
            "throw exception user already exists"
            return False
        Room.service.add(room)
        return True

    @staticmethod
    def delete(room):
        return Room.service.delete(room)

    def update(self):
        Room.service.update(self)
