from Model import Model
from services.MeetingAttendeeService import MeetingAttendeeService
from services.DatabaseService import DatabaseService


class MeetingAttendee(Model):
    __tablename__ = 'meetingattendee'
    __table_args__ = {'autoload': True, 'autoload_with': DatabaseService.DBEngine()}
    service = MeetingAttendeeService()

    def getMeeting(self):
        from models.Meeting import Meeting
        meeting = Meeting.getById(self.meeting_id)
        return meeting

    def getEmployee(self):
        from models.Employee import Employee
        employee = Employee.getById(self.employee_id)
        return employee

    @staticmethod
    def getById(id):
        meeting_attn = MeetingAttendee.service.get(id)
        return meeting_attn

    @staticmethod
    def getByMeetingId(id):
        meeting_attn = MeetingAttendee.service.getByMeetingId(id)
        return meeting_attn

    @staticmethod
    def getByEmployeeAndStatus(emp_id, ac_stat):
        meeting_attn = MeetingAttendee.service.getByEmployeeAndStatus(emp_id, ac_stat)
        return meeting_attn

    @staticmethod
    def getByMeetingAndStatus(meeting_id, ac_stat):
        meeting_attn = MeetingAttendee.service.getByMeetingAndStatus(meeting_id, ac_stat)
        return meeting_attn

    @staticmethod
    def getByMeetingAndEmployeeId(meeting_id, employee_id):
        meeting_attn = MeetingAttendee.service.getByMeetingAndEmployeeId(meeting_id, employee_id)
        return meeting_attn

    @staticmethod
    def add(meeting_attendee):
        old_meeting_attn = MeetingAttendee.service.getByMeetingAndEmployeeId(
                meeting_attendee.meeting_id, meeting_attendee.employee_id)
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
