from __future__ import print_function
from flask_login import current_user
from flask_jwt import jwt_required
from views.PageView import PageView
from flask import Response
from BaseController import BaseController
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
