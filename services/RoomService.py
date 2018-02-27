from DatabaseService import DatabaseService

class RoomService(DatabaseService):

   def get(self, id, serialize = False):
     from models.Room import Room
     room = None
     room = self.session.query(Room).get(id)
     if serialize:
        return room.serialize()
     else:
        return room

   def getById(self, room_id):
     return self.get(room_id)

   def getByName(self, name):
     from models.Room import Room
     room = None
     room = self.session.query(Room).filter(Room.name == str(name)).all()
     if(len(room)>0):
        return room[0]
     return None

   def add(self, room):
     from models.Room import Room
     if isinstance(room, Room):
        self.session.add(room)
        self.session.commit()

   def delete(self, room):
     from models.Room import Room
     if isinstance(room, Room):
        self.session.delete(room)
        self.session.commit()


   def update(self, room):
      from models.Room import Room
      if isinstance(room, Room):
          self.session.commit()
