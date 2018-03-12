from Model import Model
from services.MeetingService import MeetingService
from services.DatabaseService import DatabaseService
from datetime import datetime
from datetime import timedelta

class Meeting(Model):

   __tablename__ = 'meeting'
   __table_args__ = {'autoload':True, 'autoload_with':DatabaseService.DBEngine()}
   service = MeetingService()

   def getRoom(self):
       from models.Room import Room
       room = Room.getById(self.room_id)
       return room

   def update(self):
       Meeting.service.update(self)

   @staticmethod
   def upifyTime(meeting):
       if meeting is not None:
           meeting.end_time = meeting.end_time + timedelta(minutes=1)
       return meeting

   @staticmethod
   def getById(meet_id):
       meeting = Meeting.service.get(meet_id)
       return meeting

   @staticmethod
   def getByTime(start, end):
       meeting = Meeting.service.getByTime(start, end)
       return meeting

   @staticmethod
   def getByMeetingId(id):
       meeting= Meeting.service.getByMeetingId(id)
       return meeting

   @staticmethod
   def getByEmployeeId(emp_id):
       meeting= Meeting.service.getByEmployeeId(emp_id)
       return meeting

   @staticmethod
   def getByRoomId(room_id):
       meeting= Meeting.service.getByRoomId(room_id)
       return meeting

   @staticmethod
   def getByRoomTime(room_id, time):
       meeting = Meeting.service.getByRoomTime(room_id, time)
       return meeting

   @staticmethod
   def add(meeting):
      Meeting.service.add(meeting)
      return True

   @staticmethod
   def delete(meeting):
       return Meeting.service.delete(meeting)
