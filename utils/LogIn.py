from __future__ import print_function
from flask_login import LoginManager
from models.Employee import Employee
from models.Administrator import Administrator
from flask import Flask, session
from flask.ext.session import Session

class LogIn():

   @staticmethod
   def employee_login(app):
      emp_login = LoginManager()
      emp_login.init_app(app)
      emp_login.login_view = 'login'

      @emp_login.user_loader
      def load_user(id):
         print("loading user")
         if(session.get('user_type')):
             if(session['user_type'] == 'Employee'):
                 emp = Employee.getById(int(id))
                 if isinstance(emp, Employee) == False:
                     return None
             elif(session['user_type'] == 'Admin'):
                 emp = Administrator.getById(int(id))
                 if isinstance(emp, Administrator) == False:
                     return None

             emp.is_authenticated = True
             print(emp)
             return emp
         return None
