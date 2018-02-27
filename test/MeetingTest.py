from models.Meeting import Meeting

class MeetingTest:

    def addMeeting(self):
       meeting = Meeting()
       meeting.employee_id = 10
       meeting.room_id = 3
       meeting.start_time = "2018-11-03 01:00:00"
       meeting.end_time = "2018-11-05 01:00:00"
       print Meeting.add(meeting)

    def getMeeting(self):
       meeting = Meeting.getByEmployeeId(10)
       print meeting
       if meeting!=None:
           print meeting.room_id
           print meeting.start_time
           print meeting.end_time


    def deleteMeeting(self):
       meeting = Meeting.getByEmployeeId(10)
       print meeting
       if meeting!=None:
          print meeting.meeting_id
          Meeting.delete(meeting)

    def updateMeeting(self):
       meeting = Meeting.getByEmployeeId(10)
       print meeting
       meeting.end_time = "2018-11-15 01:00:00"
       meeting.update()

    def run(self):
       self.addMeeting()
       self.getMeeting()
       #self.deleteMeeting()
       self.updateMeeting()
