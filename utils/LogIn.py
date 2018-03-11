from __future__ import print_function
from flask_login import LoginManager
from models.Employee import Employee
from models.Administrator import Administrator

class LogIn():

   @staticmethod
   def employee_login(app):
      emp_login = LoginManager()
      emp_login.init_app(app)
      emp_login.login_view = 'login'

      @emp_login.user_loader
      def load_user(id):
         print("loading user")
         emp = Employee.getById(int(id))
         if emp is None:
             print("Get Admin")
             emp = Administrator.getById(int(id))
             if(isinstance(emp, Administrator) == False):
                 return None
             print("Got Admin")
         emp.is_authenticated = True
         print(emp)
         return emp
