from models.Meeting import Meeting


class MeetingTest:
    def addMeeting(self):
        meeting = Meeting()
        meeting.employee_id = 10
        meeting.room_id = 3
        meeting.start_time = "2018-11-03 01:00:00"
        meeting.end_time = "2018-11-05 01:00:00"
        print Meeting.add(meeting)
        print meeting.meeting_id

    def getMeeting(self):
        meeting_l = Meeting.getByEmployeeId(10)
        print meeting_l
        for meeting in meeting_l:
            print meeting.room_id
            print meeting.start_time
            print meeting.end_time
            print meeting.getRoom()

    def getByTime(self):
        start_time = "2018-11-02 9:00:00"
        end_time = "2018-11-03 11:00:00"

        meeting = Meeting.getByTime(start_time, end_time)
        for m in meeting:
            print m.room_id

    def deleteMeeting(self):
        meeting = Meeting.getByEmployeeId(10)
        print meeting
        if meeting != None:
            print meeting.meeting_id
            Meeting.delete(meeting)

    def updateMeeting(self):
        meeting = Meeting.getByEmployeeId(10)
        print meeting
        meeting.end_time = "2018-11-15 01:00:00"
        meeting.update()

    def run(self):
        # self.getByTime()
        # self.addMeeting()
        self.getMeeting()
        # self.deleteMeeting()
        # self.updateMeeting()
