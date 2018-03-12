from __future__ import print_function
from flask_login import current_user
from views.CalendarView import CalendarView
from flask import Response, redirect
from BaseController import BaseController
from models.Meeting import Meeting
from models.Employee import Employee
from models.EmployeeSchedule import EmployeeSchedule
from models.MeetingAttendee import MeetingAttendee
from utils.Time import Time
from datetime import datetime
from datetime import timedelta
from models.Timeslot import Timeslot
from flask import request

"""
 Page Controller
"""
class CalendarController(BaseController):

    def __init__(self):
        self.view = CalendarView()

    def get(self, date = datetime.now()):
        type = "g"
        if request.method == 'POST':
            type = "p"
            data_json = request.get_json(silent=True)
            start_date = Time.convertToDateTime(data_json['date'], Timeslot.getStartTime())
            end_date = Time.convertToDateTime(data_json['date'], Timeslot.getEndTime())
        else:
            now = date
            date = str(now.day) + "." + str(now.month) + "." + str(now.year)
            start_date = Time.convertToDateTime(date, Timeslot.getStartTime())
            end_date = Time.convertToDateTime(date, Timeslot.getEndTime())

        schedules = EmployeeSchedule.getByTime(current_user.employee_id, start_date, end_date)
        timeslots = self.createUnavailableTimeslots(schedules)

        return self.view.render(timeslots,start_date, schedules, type)

    def getUnavailableTimeslots(self, start_date, end_date):
        schedules = EmployeeSchedule.getByTime(current_user.employee_id, start_date, end_date)
        return self.createUnavailableTimeslots(schedules)


    def createUnavailableTimeslots(self, schedules):
        timeslots = []
        for sch in schedules:
            slot = Timeslot(sch.start_time, sch.end_time, False)
            timeslots.append(slot)
        return timeslots