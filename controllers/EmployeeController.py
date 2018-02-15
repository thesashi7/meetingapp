from __future__ import print_function
from flask.ext.login import LoginManager, UserMixin, \
                                login_required, login_user, logout_user, current_user
from flask import Flask,session, request, flash, url_for, redirect, render_template, abort ,g
from flask import render_template
from flask import Response
from BaseController import BaseController
from security.Authenticable import Authenticable
from AccountController import AccountController
from models.Employee import Employee
import sys

"""

 Parent Class Controller

"""
class EmployeeController(AccountController):

   @login_required
   def get(self):
      return render_template('calendar.html')


   def login(self):
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


   def logout(self):
      logout_user()
      return redirect("/")

   def register(self):
       pass
