from flask_login import LoginManager
from models.Employee import Employee

class LogIn():

   @staticmethod
   def employee_login(app):
      emp_login = LoginManager()
      emp_login.init_app(app)
      emp_login.login_view = 'login'

      @emp_login.user_loader
      def load_user(id):
         emp = Employee.getById(int(id))
         emp.is_authenticated = True
         return emp
