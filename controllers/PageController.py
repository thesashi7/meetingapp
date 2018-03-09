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
       from controllers.EmployeeController import EmployeeController
       if (current_user.is_authenticated == True):
          return EmployeeController().calendar()
       return self.view.render_landing()

    def schedule(self):
        return self.view.render_schedule()
