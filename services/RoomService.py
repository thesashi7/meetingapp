from DatabaseService import DatabaseService
from sqlalchemy import or_, and_


class RoomService(DatabaseService):
    def getAll(self):
        from models.Room import Room
        rooms = None
        rooms = self.session.query(Room).all()
        return rooms

    def getAllByFilter(self, room_ids):
        from models.Room import Room
        rooms = None
        rooms = self.session.query(Room).filter(~Room.room_id.in_(room_ids)).all()
        return rooms

    def getAllByFilterCapacity(self, room_ids, capacity):
        from models.Room import Room
        rooms = None
        rooms = self.session.query(Room).filter(and_(~Room.room_id.in_(room_ids),
                                                     Room.capacity >= capacity)).all()
        return rooms

    def get(self, id, serialize=False):
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
        if (len(room) > 0):
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
