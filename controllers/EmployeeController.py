from __future__ import print_function
from flask.ext.login import LoginManager, UserMixin, \
                                login_required, login_user, logout_user, current_user
from flask import Flask,session, request, flash, url_for, redirect, render_template, abort ,g
from flask import render_template
from flask import Response, request
from BaseController import BaseController
from security.Authenticable import Authenticable
from AccountController import AccountController
from PageController import PageController
from models.Employee import Employee
from views.PageView import PageView
from views.EmployeeView import EmployeeView
from models.Meeting import Meeting
from models.MeetingAttendee import MeetingAttendee
import sys

"""

 Parent Class Controller

"""
class EmployeeController(AccountController):

   def __init__(self):
      self.view = EmployeeView()

   def get(self):
      return render_template('calendar.html')


   def login(self):
      if request.method == 'POST':
          print('This standard output', file=sys.stdout)
          username = request.form['username']
          password = request.form['password']
          print('got data', file=sys.stdout)
          registered_user = Employee.getByCredential(username, password)
          if registered_user is None:
             flash('Username or Password is invalid' , 'error')
             print ('Fuck', file=sys.stdout)
             return redirect('/')
          print ('Got this shit', file=sys.stdout)
          login_user(registered_user)
          flash('Logged in successfully')
          return redirect('/calendar')
      return PageController().index()


   def logout(self):
      logout_user()
      return redirect("/")

   def register(self):
       pass
       
   def calendar(self):
       view = EmployeeView()
       return view.render_calendar()

   def setting(self):
       #check for request
       # if post then validate and update
       if request.method == 'POST':
          username = request.form['username']
          password = request.form['password']
          if len(username) >2 and len(password) > 2:
              current_user.username  = username
              current_user.setPassword(password)
              Employee.update(current_user)
              self.view.setFlashMessage("success","Successfully updated")
          else:
            self.view.setFlashMessage("fail","Update Failed!")
       return self.view.render_employee_setting(current_user)

   def dashboard(self):
       owned_m = Meeting.getByEmployeeId(current_user.employee_id)
       pending = MeetingAttendee.getByEmployeeAndStatus(current_user.employee_id, 'P')
       accepted = MeetingAttendee.getByEmployeeAndStatus(current_user.employee_id, 'Y')
       if owned_m is not None:
          for m in owned_m:
              print(m.end_time.year)
       if pending is not None:
          for m in pending:
              print(m)
              print(m.getMeeting().end_time)
       return self.view.render_dashboard(owned_m, pending, accepted)
