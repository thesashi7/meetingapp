from models.Room import Room


class RoomTest:
    def addRoom(self):
        room = Room()
        room.name = "ac12"
        room.capacity = 12
        print Room.add(room)

    def getRoom(self):
        room = Room.getByName("ac12")
        print room
        if room != None:
            print room.name
            print room.room_id
            print room.capacity

    def deleteRoom(self):
        room = Room.getByName("ac12")
        print room
        if room != None:
            print room.room_id
            Room.delete(room)

    def updateRoom(self):
        room = Room.getByName("ac12")
        print room
        room.capacity = 91
        room.update()

    def run(self):
        self.addRoom()
        self.getRoom()
        # self.deleteRoom()
        self.updateRoom()
