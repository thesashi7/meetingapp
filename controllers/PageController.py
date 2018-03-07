from __future__ import print_function
from flask_login import current_user
from views.PageView import PageView
from flask import Response, redirect
from BaseController import BaseController
from models.Meeting import Meeting
from models.MeetingAttendee import MeetingAttendee
import sys

"""
 Page Controller
"""
class PageController(BaseController):

    def __init__(self):
        self.view = PageView()

    def index(self):
       if (current_user.is_authenticated == True):
          return self.view.render_calendar()
       return self.view.render_landing()

    def schedule(self):
        return self.view.render_schedule()

    def dashboard(self):
        owned_m = Meeting.getByEmployeeId(current_user.employee_id)
        pending = MeetingAttendee.getByEmployeeAndStatus(current_user.employee_id, 'N')
        accepted = MeetingAttendee.getByEmployeeAndStatus(current_user.employee_id, 'Y')
        for m in owned_m:
            print(m.end_time.year)
        return self.view.render_dashboard(owned_m, pending, accepted)
