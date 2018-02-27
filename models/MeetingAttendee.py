from Model import Model
from services.MeetingAttendeeService import MeetingAttendeeService
from services.DatabaseService import DatabaseService

class MeetingAttendee(Model):

   __tablename__ = 'meetingattendee'
   __table_args__ = {'autoload':True, 'autoload_with':DatabaseService.DBEngine()}
   service = MeetingAttendeeService()


   @staticmethod
   def getByMeetingId(id):
       meeting_attn= MeetingAttendee.service.getByMeetingId(id)
       return meeting_attn

   @staticmethod
   def getByMeetingAndEmployeeId(meeting_id, employee_id):
       meeting_attn = MeetingAttendee.service.getByMeetingAndEmployeeId(meeting_id, employee_id)
       return meeting_attn

   @staticmethod
   def add(meeting_attendee):
      old_meeting_attn = MeetingAttendee.service.getByMeetingAndEmployeeId(
        meeting_attendee.meeting_id,meeting_attendee.employee_id)
      if (old_meeting_attn is not None):
         "throw exception user already exists"
         return False
      MeetingAttendee.service.add(meeting_attendee)
      return True

   @staticmethod
   def delete(meeting_attendee):
       return MeetingAttendee.service.delete(meeting_attendee)

   def update(self):
       MeetingAttendee.service.update(self)
