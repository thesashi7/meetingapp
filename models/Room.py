from Model import Model
from services.RoomService import RoomService
from services.DatabaseService import DatabaseService

class Room(Model):

   __tablename__ = 'room'
   __table_args__ = {'autoload':True, 'autoload_with':DatabaseService.DBEngine()}
   service = RoomService()


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
