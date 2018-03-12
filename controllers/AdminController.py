from __future__ import print_function
from views.PageView import PageView
from flask.ext.login import LoginManager, UserMixin, \
                                login_required, login_user, logout_user, current_user
from flask import Flask,session,request, redirect, render_template
from flask import Response, request
from models.Administrator import Administrator
from models.Employee import Employee
from models.Room import Room
from models.Meeting import Meeting
from models.MeetingAttendee import  MeetingAttendee
from models.EmployeeSchedule import EmployeeSchedule
from models.Notification import Notification
from BaseController import BaseController
from MeetingController import MeetingController
from security.Authenticable import Authenticable
import sys
from flask import Flask, session
from flask.ext.session import Session
from datetime import datetime

class AdminController(BaseController):
    def adminaddroom(self):
        view = PageView()
        if request.method == 'POST':
            print(request.form['room_name']+" "+request.form['capacity'])
            room = Room()
            room.name = request.form['room_name']
            room.capacity = request.form['capacity']
            Room.add(room)
            print("submitted")
            view.setFlashMessage("success", "Room has been saved")
        return view.render_admin_add_room()


    def adminaddemp(self):
        view = PageView()
        if request.method == 'POST':
            print(request.form['username']+" "+request.form['password'])
            emp = Employee()
            emp.setCredentials(request.form['username'], request.form['password'])
            emp.visible = "Y"
            Employee.add(emp)
            print("submitted")
            view.setFlashMessage("success", "Employee has been saved")
        return view.render_admin_add_emp()


    def adminconfigroom(self):
        view = PageView()
        if request.method == 'POST':
            print(request.form['name']+" "+request.form['capacity'])
            room = Room.getById(request.form['room_id'])
            if(room.name != request.form['name']):
                exist_room = Room.getByName(request.form['name'])
                if isinstance(exist_room, Room):
                    return "Room name alreayd exists!"
            room.name = request.form['name']
            room.capacity = request.form['capacity']
            room.update()
            print("submitted")
            return "Saved"
        else:
            rooms = Room.getAll()
            return view.render_admin_config_room(rooms)


    def adminconfigemp(self):
        view = PageView()
        if request.method == 'POST':
            print(request.form['username']+" "+request.form['password'])
            emp = Employee.getById(request.form['employee_id'])
            if(emp.username != request.form['username']):
                exist_emp = Employee.getByUsername(request.form['username'])
                if isinstance(exist_emp, Employee):
                    return "Username alreayd exists!"
            emp.setCredentials(request.form['username'], request.form['password'])
            emp.visible = "Y"
            emp.update()
            print("submitted")
            return "Saved"
        else:
            employees = Employee.getAll()
            return view.render_admin_config_emp(employees)

    def deleteAllMeetings(self, meetings):
        if meetings is not None:
            meet_c = MeetingController()
            for meet in meetings:
                meet_c.deleteMeeting(meet.meeting_id)

    def deleteRoom(self):
        meetings = Meeting.getByRoomId(request.form['room_id'])
        self.deleteAllMeetings(meetings)
        room = Room.getById(request.form['room_id'])
        if isinstance(room, Room):
            Room.delete(room)
            return "Deleted"
        return "Room does not exist"

    def deleteEmployee(self):
        employee = Employee.getById(request.form['employee_id'])
        if isinstance(employee, Employee):
            meetings = Meeting.getByEmployeeId(request.form['employee_id'])
            invites = MeetingAttendee.getByEmployeeId(request.form['employee_id'])
            schs = EmployeeSchedule.getByEmployeeId(request.form['employee_id'])
            notfs = Notification.getByEmployeeId(request.form['employee_id'])
            self.deleteAllMeetings(meetings)
            if invites is not None:
                for inv in invites:
                    MeetingAttendee.delete(inv)
            if schs is not None:
                for sc in schs:
                    EmployeeSchedule.delete(sc)
            if notfs is not None:
                for notf in notfs:
                    Notification.delete(notf)

            Employee.delete(employee)
            return "Deleted"
        return "Employee does not exist"

    def adminlogin(self):
        view = PageView()
        if request.method == 'POST':
            print('This standard output', file=sys.stdout)
            username = request.form['username']
            password = request.form['password']
            print("oooo")
            print("uu-->"+request.form['username']+" "+request.form['password'])
            print('got data', file=sys.stdout)
            registered_user = Administrator.getByCredential(username, password)
            if registered_user is None:
                #flash('Username or Password is invalid' , 'error')
                print ('Fuck', file=sys.stdout)
                return redirect('admin_login')
            print ('Got this shit', file=sys.stdout)
            print ("fffuuuc")
            session['user_type'] = "Admin"
            print(registered_user)
            login_user(registered_user)
            #flash('Logged in successfully')
            return redirect('/admin_config_emp')
        if (current_user.is_authenticated == True and isinstance(current_user, Administrator)):
            return redirect('/admin_config_emp')
        return view.render_admin_login()

    def setting(self):
       view = PageView()
       #check for request
       # if post then validate and update
       if request.method == 'POST':
          if(request.form['type'] == 'credential'):
              username = request.form['username']
              password = request.form['password']
              if len(username) >2 and len(password) > 2:
                  if(username != current_user.username):
                      exist = Administrator.getByUsername(username)
                      if isinstance(exist, Administrator):
                          view.setFlashMessage("fail","Username already exists!")
                          return view.render_admin_setting(current_user)

                  current_user.username  = username
                  current_user.setPassword(password)
                  current_user.update()
                  view.setFlashMessage("success","Successfully updated")
              else:
                  view.setFlashMessage("fail","Password must be greater than 2!")
       return view.render_admin_setting(current_user)
