from models.MeetingAttendee import MeetingAttendee


class MeetingAttendeeTest:
    def addMeetingAttendee(self):
        meeting_attn = MeetingAttendee()
        meeting_attn.employee_id = 10
        meeting_attn.meeting_id = 3
        meeting_attn.accepted = "N"
        meeting_attn.notified = "N"
        print MeetingAttendee.add(meeting_attn)

    def getByMeetingAttendee(self):
        meeting_attn = MeetingAttendee.getByMeetingAndEmployeeId(10, 3)
        print meeting_attn
        if meeting_attn != None:
            print meeting_attn.employee_id
            print meeting_attn.meeting_id
            print meeting_attn.accepted

    def deleteMeetingAttendee(self):
        meeting_attn = MeetingAttendee.getByEmployeeAndMeetingId(10, 3)
        print meeting_attn
        if meeting_attn != None:
            print meeting_attn.meeting_attendee_id
            MeetingAttendee.delete(meeting_attn)

    def updateMeetingAttendee(self):
        meeting_attn = MeetingAttendee.getByEmployeeAndMeetingId(10, 3)
        print meeting_attn
        meeting_attn.accepted = "Y"
        meeting_attn.notified = "Noooo"
        meeting_attn.update()

    def run(self):
        self.addMeetingAttendee()
        self.getByMeetingAttendee()
        # self.deleteMeetingAttendee()
        self.updateMeetingAttendee()
