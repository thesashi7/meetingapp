from __future__ import print_function
from flask.ext.login import LoginManager, UserMixin, \
                                login_required, login_user, logout_user, current_user
from views.PageView import PageView
from views.EmployeeView import EmployeeView
from models.Meeting import Meeting
from models.MeetingAttendee import MeetingAttendee
from models.EmployeeSchedule import EmployeeSchedule
from models.Employee import Employee
from models.Notification import Notification
from models.Room import Room
from datetime import datetime
from datetime import timedelta
from EmployeeController import EmployeeController
from utils.Time import Time

class MeetingController():

    #create
    #update
    #delete

    def create(self, data_json):
        new_meeting = Meeting()

        new_meeting.employee_id = current_user.employee_id
        new_meeting.room_id = data_json['room']
        year = data_json['date']
        start_time = data_json['start']
        end_time = data_json['end']
        start_date = datetime.strptime(year+" "+start_time, '%m.%d.%Y %I:%M %p')
        end_date = datetime.strptime(year+" "+end_time, '%m.%d.%Y %I:%M %p')
        new_meeting.start_time = start_date
        new_meeting.end_time = end_date
        Meeting.add(new_meeting)
        for em in data_json['selected']:
            for attribute, value in em.iteritems():
                meeting_attn = MeetingAttendee()
                meeting_attn.meeting_id = new_meeting.meeting_id
                meeting_attn.employee_id = value
                meeting_attn.accepted = "P"


                notification = Notification()
                notification.employee_id = value
                notification.active = "Y"
                notification.message = "Meeting Request from "+current_user.username
                Notification.add(notification)
                meeting_attn.notification_id = notification.notification_id
                MeetingAttendee.add(meeting_attn)
                print (attribute, value)
        print("----------------------")
        print(data_json['start'])
        print(data_json['selected'])
        print("----------------------")
        #Meeting.add(new_meeting)

        view = EmployeeView()
        return view.render_meeting_confirm(False)

    def update(self):
        pass

    def cancelMeeting(self, meeting_id):
       meeting = Meeting.getById(meeting_id)
       # get all the meeting attendees
       #  and send them all notification of cancelation
       attendees = MeetingAttendee.getByMeetingId(meeting_id)
       print (attendees)
       for att in attendees:
           print (att)
           if att.accepted == "Y":
               notification = Notification()
               notification.employee_id = att.employee_id
               notification.message = "Meeting from "+str(meeting.start_time)+" to "+str(meeting.end_time)+" is cancelled"
               notification.active = "Y"
               Notification.add(notification)
           # need to delete previous meeting associated with this meeting
           past_notifications = Notification.getByMeetingId(att.meeting_id)
           print (past_notifications)
           for past_notification in past_notifications:
               Notification.delete(past_notification)
           MeetingAttendee.delete(att)

       Meeting.delete(meeting)
       return EmployeeController().dashboard()

    def schedule(self):
        print(current_user)
        print("loggedIN:"+str(current_user.employee_id))
        view = EmployeeView()
        emp_list = Employee.getAllExcluding([current_user.employee_id])
        return view.render_schedule_add_emp(emp_list)

    # check for emp schedule
    def validateAttendeesTime(self, data_json):
        print(data_json)
        start_date = Time.convertToDateTime(data_json['date'],data_json['start'])
        end_date = Time.convertToDateTime(data_json['date'], data_json['end'])
        end_date = end_date - timedelta(minutes = 1)
        avail = True
        for em in data_json['selected']:
            for attribute, value in em.iteritems():
                if (EmployeeSchedule.isAvailable(value, start_date, end_date) == False):
                    avail = False
                    break
        if avail == False:
            # need to render calendar with avail slots
            return EmployeeView().render_schedule_calendar(data_json)
        print("--------True --------------")
        return self.scheduleRoom(data_json)

    def scheduleTime(self, emp_json):
        #get emp overlapping avail times using emp_json

        view = EmployeeView()
        emp_list = Employee.getAll()
        return view.render_schedule_add_emp(emp_list)

    def scheduleRoom(self, time_json):
        view = EmployeeView()
        # get time within postgre format
        print(time_json)
        year = time_json['date']
        start_time = time_json['start']
        end_time = time_json['end']
        print (year)
        start_date = Time.convertToDateTime(year, start_time)
        end_date = Time.convertToDateTime(year, end_time)

        print (start_date)
        print (end_date)
        end_date = end_date - timedelta(minutes = 1)
        # get all meetings within than time range
        # filter all the rooms that are occupied
        room_list = Room.getAvailableRooms(start_date, end_date)
        print(room_list)

        return view.render_schedule_add_room(room_list)

    def createEmployeeSchedule(self, employee_id, meeting):
        employee_schedule = EmployeeSchedule()
        employee_schedule.employee_id = employee_id
        employee_schedule.start_time = meeting.start_time
        employee_schedule.end_time = meeting.end_time
        employee_schedule.available = "N"
        EmployeeSchedule.add(employee_schedule)

    def acceptMeeting(self, meeting_att_id):
        meeting_att = MeetingAttendee.getById(meeting_att_id)
        meeting_att.accepted = "Y"
        meeting_att.update()
        meeting = Meeting.getById(meeting_att.meeting_id)
        self.createEmployeeSchedule(meeting_att.employee_id, meeting)

        #create Notification
        notification = Notification()
        print (notification)
        notification.employee_id = meeting.employee_id
        notification.active = "Y"
        attendee = Employee.getById(meeting_att.employee_id)
        notification.message = attendee.username+" has accepted your request for meeting from "+str(meeting.start_time)+" to "+str(meeting.end_time)
        notification.meeting_id = meeting_att.meeting_id
        Notification.add(notification)

        # need to update current notification of this employee
        past_notification = Notification.getById(meeting_att.notification_id)
        past_notification.active = "N"
        past_notification.update()
        return EmployeeController().dashboard()

    def declineMeeting(self, meeting_att_id):
        meeting_att = MeetingAttendee.getById(meeting_att_id)
        meeting_att.accepted = "N"
        meeting_att.update()
        meeting = Meeting.getById(meeting_att.meeting_id)
        notification = Notification()
        print (notification)
        notification.employee_id = meeting.employee_id
        notification.active = "Y"
        attendee = Employee.getById(meeting_att.employee_id)
        notification.message = attendee.username+" has declined your request for meeting from "+str(meeting.start_time)+" to "+str(meeting.end_time)
        notification.meeting_id = meeting_att.meeting_id

        Notification.add(notification)
        # need to update current notification of this employee
        past_notification = Notification.getById(meeting_att.notification_id)
        past_notification.active = "N"
        past_notification.update()
        return EmployeeController().dashboard()
