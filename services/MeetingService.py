from __future__ import print_function
from DatabaseService import DatabaseService
from sqlalchemy import or_, and_
class MeetingService(DatabaseService):

   def get(self, id, serialize = False):
     from models.Meeting import Meeting
     meeting = None
     meeting = self.session.query(Meeting).get(id)
     if serialize:
        return meeting.serialize()
     else:
        return meeting

   def getById(self, meeting_id):
     return self.get(meeting_id)

   def getByEmployeeId(self, emp_id):
     from models.Meeting import Meeting
     meeting= None
     meeting= self.session.query(Meeting).filter(Meeting.employee_id == str(emp_id)).all()
     if(len(meeting)>0):
        return meeting
     return None

   def getByTime(self, start, end):
       from models.Meeting import Meeting
       meeting = None
       meeting = self.session.query(Meeting).filter(or_(
          and_(Meeting.start_time <= start, Meeting.end_time >= start),
          and_(Meeting.start_time <= end, Meeting.end_time >= end))).all()
       return meeting

   def add(self, meeting):
     from models.Meeting import Meeting
     if isinstance(meeting, Meeting):
        self.session.add(meeting)
        self.session.commit()
        print (meeting.meeting_id)

   def delete(self, meeting):
     from models.Meeting import Meeting
     if isinstance(meeting, Meeting):
        self.session.delete(meeting)
        self.session.commit()


   def update(self, meeting):
      from models.Meeting import Meeting
      if isinstance(meeting, Meeting):
          self.session.commit()
