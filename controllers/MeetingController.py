from __future__ import print_function
from flask.ext.login import LoginManager, UserMixin, \
    login_required, login_user, logout_user, current_user
from views.PageView import PageView
from models.Meeting import Meeting
from models.MeetingAttendee import MeetingAttendee
from models.Employee import Employee
from models.Room import Room
from datetime import datetime
from datetime import timedelta
from PageController import PageController


class MeetingController():
    # create
    # update
    # delete

    def create(self, data_json):
        new_meeting = Meeting()

        new_meeting.employee_id = current_user.employee_id
        new_meeting.room_id = data_json['room']
        year = data_json['date']
        start_time = data_json['start']
        end_time = data_json['end']
        start_date = datetime.strptime(year + " " + start_time, '%m.%d.%Y %I:%M %p')
        end_date = datetime.strptime(year + " " + end_time, '%m.%d.%Y %I:%M %p')
        new_meeting.start_time = start_date
        new_meeting.end_time = end_date
        Meeting.add(new_meeting)
        for em in data_json['selected']:
            for attribute, value in em.iteritems():
                meeting_attn = MeetingAttendee()
                meeting_attn.meeting_id = new_meeting.meeting_id
                meeting_attn.employee_id = value
                meeting_attn.accepted = "N"
                meeting_attn.notified = "N"
                MeetingAttendee.add(meeting_attn)
                print(attribute, value)
        print("----------------------")
        print(data_json['start'])
        print(data_json['selected'])
        print("----------------------")
        # Meeting.add(new_meeting)

        view = PageView()
        return view.render_meeting_confirm(False)

    def update(self):
        pass

    def cancelMeeting(self, meeting_id):
        meeting = Meeting.getById(meeting_id)
        Meeting.delete(meeting)
        return PageController().dashboard()

    def schedule(self):
        print(current_user)
        print("loggedIN:" + str(current_user.employee_id))
        view = PageView()
        emp_list = Employee.getAllExcluding([current_user.employee_id])
        return view.render_schedule_add_emp(emp_list)

    def scheduleTime(self, emp_json):
        # get emp overlapping avail times using emp_json

        view = PageView()
        emp_list = Employee.getAll()
        return view.render_schedule_add_emp(emp_list)

    def scheduleRoom(self, time_json):
        view = PageView()
        # get time within postgre format
        print(time_json)
        year = time_json['date']
        start_time = time_json['start_time']
        end_time = time_json['end_time']
        print(year)
        start_date = datetime.strptime(year + " " + start_time, '%m.%d.%Y %I:%M %p')
        end_date = datetime.strptime(year + " " + end_time, '%m.%d.%Y %I:%M %p')
        print(start_date)
        print(end_date)
        end_date = end_date - timedelta(minutes=1)
        # get all meetings within than time range
        # filter all the rooms that are occupied
        room_list = Room.getAvailableRooms(start_date, end_date)
        print(room_list)

        return view.render_schedule_add_room(room_list)
