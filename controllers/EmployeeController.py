from __future__ import print_function
from flask.ext.login import LoginManager, UserMixin, \
                                login_required, login_user, logout_user, current_user
from flask import Flask,session, request, flash, url_for, redirect
from flask import render_template
from flask import Response, request
from BaseController import BaseController
from security.Authenticable import Authenticable
from AccountController import AccountController
from PageController import PageController
from models.Employee import Employee
from models.EmployeeSchedule import EmployeeSchedule
from views.PageView import PageView
from views.EmployeeView import EmployeeView
from models.Meeting import Meeting
from models.MeetingAttendee import MeetingAttendee
import sys
from flask import Flask, session
from flask.ext.session import Session
from utils.Time import Time

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
          print(username+" "+password)
          registered_user = Employee.getByCredential(username, password)
          if registered_user is None:
             flash('Username or Password is invalid' , 'error')
             print ('Fuck', file=sys.stdout)
             return redirect('/')
          print ('Got this shit', file=sys.stdout)
          session['user_type'] = "Employee"
          login_user(registered_user)
          print("logged IN")
          print(current_user)
          flash('Logged in successfully')
          return redirect('/calendar')
      return PageController().index()


   def logout(self):
      logout_user()
      return redirect("/")

   def register(self):
       pass

   def addEvent(self):
       info = request.form['info']
       date = request.form['date']
       start_time = Time.convertToDateTime(date,request.form['start'])
       end_time =  Time.convertToDateTime(date,request.form['end'])
       if(EmployeeSchedule.isAvailable(current_user.employee_id, start_time,end_time)):
           emp_s = EmployeeSchedule()
           emp_s.employee_id = current_user.employee_id
           emp_s.start_time = start_time
           emp_s.end_time = end_time
           emp_s.available = "N"
           emp_s.info = info
           EmployeeSchedule.add(emp_s)
           return "Saved"
       return "You already have other events planned for this time"

   def updateEvent(self):
       info = request.form['info']
       date = request.form['date']
       start_time = Time.convertToDateTime(date,request.form['start'])
       end_time =  Time.convertToDateTime(date,request.form['end'])
       schedules = EmployeeSchedule.getByTime(current_user.employee_id, start_time,end_time)
       conflict = False
       for sch in schedules:
           print (str(sch.employee_schedule_id )+" ? "+request.form['id'])
           if str(sch.employee_schedule_id) != str(request.form['id']):
               conflict = True
               break
       if(conflict is False):
           emp_s = EmployeeSchedule.getByEmployeeScheduleId(request.form['id'])
           emp_s.start_time = start_time
           emp_s.end_time = end_time
           emp_s.available = "N"
           emp_s.info = info
           emp_s.update()
           return "Saved"
       return "You already have other events planned for this time"

   def deleteEvent(self):
       emp_s = EmployeeSchedule.getByEmployeeScheduleId(request.form['id'])
       if isinstance(emp_s, EmployeeSchedule) and emp_s.info != "Meeting":
           EmployeeSchedule.delete(emp_s)
           return "Deleted"
       return "Unable to delete!"


   def setting(self):
       #check for request
       # if post then validate and update
       if request.method == 'POST':
          if(request.form['type'] == 'credential'):
              username = request.form['username']
              password = request.form['password']
              if len(username) >2 and len(password) > 2:
                  if(username != current_user.username):
                      exist = Employee.getByUsername(username)
                      if isinstance(exist, Employee):
                          self.view.setFlashMessage("fail","Username already exists!")
                          return self.view.render_employee_setting(current_user)

                  current_user.username  = username
                  current_user.setPassword(password)
                  current_user.update()
                  self.view.setFlashMessage("success","Successfully updated")
              else:
                  self.view.setFlashMessage("fail","Password must be greater than 2!")
          elif(request.form['type'] == 'visible'):
              current_user.visible = request.form['visible']
              current_user.update()
              self.view.setFlashMessage("success","Successfully updated")
          elif(request.form['type'] == 'profile'):
              current_user.first_name = request.form['first_name']
              current_user.last_name = request.form['last_name']
              current_user.update()
              self.view.setFlashMessage("success","Successfully updated")

       return self.view.render_employee_setting(current_user)

   def dashboard(self):
       owned_m = Meeting.getByEmployeeId(current_user.employee_id)
       pending = MeetingAttendee.getByEmployeeAndStatus(current_user.employee_id, 'P')
       accepted = MeetingAttendee.getByEmployeeAndStatus(current_user.employee_id, 'Y')
       meet_att_map = {}
       if owned_m is not None:
          for m in owned_m:
              attendees = MeetingAttendee.getByMeetingId(m.meeting_id)
              meet_att_map[m.meeting_id] = attendees

              #print(m.end_time.year)
       if pending is not None:
          for m in pending:
              print(m)
              print(m.getMeeting().end_time)
       return self.view.render_dashboard(owned_m, pending, accepted, meet_att_map)
