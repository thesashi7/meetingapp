from __future__ import print_function
from controllers.PageController import PageController
from controllers.MeetingController import MeetingController
from controllers.EmployeeController import EmployeeController
from index import app
import sys
from models.Employee import Employee
from flask_login import logout_user, login_required
from flask import request

@app.route('/')
def index():
    return PageController().index()

@app.route('/calendar')
@login_required
def calendar():
    return EmployeeController().get()

@app.route('/login', methods=['POST', 'GET'])
def login():
    return EmployeeController().login()


@app.route('/logout')
def logout():
   return EmployeeController().logout()

@app.route('/schedule', methods=['POST','GET'])
@login_required
def schedule():
   req = request.form.get('step')
   content = request.get_json(silent=True)
   print (content)
   print(req)
   return MeetingController().schedule()

@app.route('/scheduletime', methods=['POST'])
@login_required
def schedule_time():
   req = request.form.get('step')
   content = request.get_json(silent=True)
   print("--------------------------------------------")
   print (content)
   print(req)
   return MeetingController().scheduleTime(content)

@app.route('/scheduleroom', methods=['POST'])
@login_required
def schedule_room():
   content = request.get_json(silent=True)
   print("==================================")
   print (content)
   #validate and schedule
   return MeetingController().validateAttendeesTime(content)

@app.route('/submitmeeting', methods=['POST'])
@login_required
def sumbit_meeting():
   content = request.get_json(silent=True)
   #print("--------------------------------------------")
   #print (content)
   return MeetingController().create(content)

@app.route('/dashboard')
@login_required
def dashboard():
    return EmployeeController().dashboard()

@app.route('/cancelmeeting', methods=['POST'])
@login_required
def cancel_meeting():
    print(request.form.get('meeting_id'))
    return MeetingController().cancelMeeting(request.form.get('meeting_id'))

@app.route('/emp-setting',methods=['GET', 'POST'])
@login_required
def emp_setting():
    return EmployeeController().setting()

@app.route('/acceptmeeting',methods=['POST'])
@login_required
def acceptMeeting():
    return MeetingController().acceptMeeting(request.form.get('meeting_attendee_id'))

@app.route('/declinemeeting',methods=['POST'])
@login_required
def declineMeeting():
    return MeetingController().declineMeeting(request.form.get('meeting_attendee_id'))
