from DatabaseService import DatabaseService

class MeetingAttendeeService(DatabaseService):

   def get(self, id, serialize = False):
     from models.MeetingAttendee import MeetingAttendee
     meeting_att= None
     meeting_att= self.session.query(MeetingAttendee).get(id)
     if serialize:
        return room.serialize()
     else:
        return room

   def getByMeetingId(self, meeting_id):
     from models.MeetingAttendee import MeetingAttendee
     meeting_att= None
     meeting_att= self.session.query(MeetingAttendee).filter(MeetingAttendee.meeting_id == str(meeting_id)).all()
     return meeting_att

   def getByEmployeeId(self, emp_id):
     from models.MeetingAttendee import MeetingAttendee
     meeting_att= None
     meeting_att= self.session.query(MeetingAttendee).filter(MeetingAttendee.employee_id == str(emp_id)).all()
     return meeting_att

   def getByMeetingAndEmployeeId(self, meeting_id, employee_id):
     from models.MeetingAttendee import MeetingAttendee
     meeting_att= None
     meeting_att= self.session.query(MeetingAttendee).filter(MeetingAttendee.meeting_id == str(meeting_id)).\
      filter(MeetingAttendee.employee_id == str(employee_id)).all()
     if (len(meeting_att)>0):
         return meeting_att[0]
     return None


   def add(self, meeting_attendee):
     from models.MeetingAttendee import MeetingAttendee
     if isinstance(meeting_attendee, MeetingAttendee):
        self.session.add(meeting_attendee)
        self.session.commit()

   def delete(self, meeting_attendee):
     from models.MeetingAttendee import MeetingAttendee
     if isinstance(meeting_attendee, MeetingAttendee):
        self.session.delete(meeting_attendee)
        self.session.commit()


   def update(self, meeting_attendee):
      from models.MeetingAttendee import MeetingAttendee
      if isinstance(meeting_attendee, MeetingAttendee):
          self.session.commit()
