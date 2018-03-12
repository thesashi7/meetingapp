from __future__ import print_function
from flask.ext.login import current_user
from controllers.PageController import PageController
from controllers.MeetingController import MeetingController
from controllers.EmployeeController import EmployeeController
from controllers.NotificationController import NotificationController
from controllers.AdminController import AdminController
from controllers.CalendarController import  CalendarController
from index import app
import sys
from models.Employee import Employee
from flask_login import logout_user, login_required
from flask import request

@app.route('/')
def index():
    return PageController().index()

@app.route('/calendar', methods=['POST', 'GET'])
@login_required
def calendar():
    if isAdmin() is False:
        print (" YYYYYYY")
        return CalendarController().get()
    return index()

@app.route('/login', methods=['POST', 'GET'])
def login():
    return EmployeeController().login()


@app.route('/logout')
def logout():
   return EmployeeController().logout()

@app.route('/schedule', methods=['POST','GET'])
@login_required
def schedule():
   if(isAdmin() is False):
       req = request.form.get('step')
       content = request.get_json(silent=True)
       print (content)
       print(req)
       return MeetingController().schedule()
   return index()

@app.route('/scheduletime', methods=['POST'])
@login_required
def schedule_time():
    if(isAdmin() is False):
        req = request.form.get('step')
        content = request.get_json(silent=True)
        print("--------------------------------------------")
        print (content)
        print(req)
        return MeetingController().scheduleTime(content)
    return index()

@app.route('/scheduleroom', methods=['POST'])
@login_required
def schedule_room():
    if(isAdmin() == False):
        content = request.get_json(silent=True)
        print("==================================")
        print (content)
        #validate and schedule
        return MeetingController().validateAttendeesTime(content)
    return index()

@app.route('/submitmeeting', methods=['POST'])
@login_required
def sumbit_meeting():
    if(isAdmin() is False):
        content = request.get_json(silent=True)
        #print("--------------------------------------------")
        #print (content)
        return MeetingController().create(content)
    return index()

@app.route('/dashboard')
@login_required
def dashboard():
    if(isAdmin() is False):
        return EmployeeController().dashboard()
    return index()

@app.route('/cancelmeeting', methods=['POST'])
@login_required
def cancel_meeting():
    if(isAdmin() is False):
        print(request.form.get('meeting_id'))
        return MeetingController().cancelMeeting(request.form.get('meeting_id'))
    return "Not allowed"

@app.route('/emp-setting',methods=['GET', 'POST'])
@login_required
def emp_setting():
    if(isAdmin() is False):
        return EmployeeController().setting()
    return index()

@app.route('/acceptmeeting',methods=['POST'])
@login_required
def acceptMeeting():
    if(isAdmin() is False):
        return MeetingController().acceptMeeting(request.form.get('meeting_attendee_id'))
    return "Not allowed"

@app.route('/declinemeeting',methods=['POST'])
@login_required
def declineMeeting():
    if(isAdmin() is False):
        return MeetingController().declineMeeting(request.form.get('meeting_attendee_id'))
    return "Not allowed"

@app.route('/notify', methods=['GET','POST'])
@login_required
def notifications():
    if(isAdmin() is False):
        return NotificationController().get()
    return index()

@app.route('/notify/seen', methods=['POST'])
@login_required
def notificationUpdate():
    if(isAdmin() is False):
        return NotificationController().update(request.form.get('notification_id'))
    return "Not allowed"

@app.route('/addevent', methods=['POST'])
@login_required
def addEvent():
    if(isAdmin() is False):
        return EmployeeController().addEvent()
    return "Not allowed"

@app.route('/updateevent', methods=['POST'])
@login_required
def updateEvent():
    if(isAdmin() is False):
        return EmployeeController().updateEvent()
    return "Not allowed"


@app.route('/deleteevent', methods=['POST'])
@login_required
def deleteEvent():
    if(isAdmin() is False):
        return EmployeeController().deleteEvent()
    return "Not allowed"

#admin stuff

@app.route('/admin_add_room', methods=['GET','POST'])
@login_required
def adminaddroom():
    print("ok ----------------------")
    if(isAdmin()):
        return AdminController().adminaddroom()
    return AdminController().adminlogin()

@app.route('/admin_add_emp' , methods=['GET','POST'])
@login_required
def adminaddemp():
    if(isAdmin()):
        return AdminController().adminaddemp()
    return AdminController().adminlogin()

@app.route('/admin_config_room', methods=['GET','POST'])
@login_required
def adminconfigroom():
    if(isAdmin()):
        return AdminController().adminconfigroom()
    return AdminController().adminlogin()

@app.route('/admin_config_emp', methods=['GET','POST'])
@login_required
def adminconfigemp():
    if(isAdmin()):
        return AdminController().adminconfigemp()
    return AdminController().adminlogin()

@app.route('/admin_login', methods=['GET','POST'])
def adminlogin():
    return AdminController().adminlogin()

@app.route('/delete_room', methods=['POST'])
@login_required
def deleteRoom():
    if(isAdmin()):
        return AdminController().deleteRoom()
    return AdminController().adminlogin()

@app.route('/delete_emp', methods=['POST'])
@login_required
def deleteEmployee():
    if(isAdmin()):
        return AdminController().deleteEmployee()
    return AdminController().adminlogin()

@app.route('/admin_setting', methods=['POST','GET'])
@login_required
def adminSetting():
    if(isAdmin()):
        return AdminController().setting()
    return AdminController().adminlogin()

def isAdmin():
    from models.Administrator import Administrator
    ad = Administrator()
    print("checking for Admin ?")
    if isinstance(current_user._get_current_object(), Administrator) == True:
        return True
    print("Not Admin")
    return False
