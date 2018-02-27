from DatabaseService import DatabaseService

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
        return meeting[0]
     return None


   def add(self, meeting):
     from models.Meeting import Meeting
     if isinstance(meeting, Meeting):
        self.session.add(meeting)
        self.session.commit()

   def delete(self, meeting):
     from models.Meeting import Meeting
     if isinstance(meeting, Meeting):
        self.session.delete(meeting)
        self.session.commit()


   def update(self, meeting):
      from models.Meeting import Meeting
      if isinstance(meeting, Meeting):
          self.session.commit()
