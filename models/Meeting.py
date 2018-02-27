from Model import Model
from services.MeetingService import MeetingService
from services.DatabaseService import DatabaseService

class Meeting(Model):

   __tablename__ = 'meeting'
   __table_args__ = {'autoload':True, 'autoload_with':DatabaseService.DBEngine()}
   service = MeetingService()


   @staticmethod
   def getByMeetingId(id):
       meeting= Meeting.service.getByMeetingId(id)
       return meeting

   @staticmethod
   def getByEmployeeId(emp_id):
       meeting= Meeting.service.getByEmployeeId(emp_id)
       return meeting

   @staticmethod
   def add(meeting):
      old_meeting = Meeting.service.getByEmployeeId(
        meeting.employee_id)
      if (old_meeting is not None):
         "throw exception user already exists"
         return False
      Meeting.service.add(meeting)
      return True

   @staticmethod
   def delete(meeting):
       return Meeting.service.delete(meeting)

   def update(self):
       Meeting.service.update(self)
