from Model import Model
from sqlalchemy.orm import relationship
from Model import Model
from services.EmployeeService import EmployeeService
from services.DatabaseService import DatabaseService
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin



class Employee(Model, UserMixin):
   __tablename__ = 'employee'
   __table_args__ = {'autoload':True, 'autoload_with':DatabaseService.DBEngine()}

   def __init__():
      self.is_authenticated = True

   def setCredentials(self, username, passw):
       self.username = username
       self.setPassword(passw)

   def setPassword(self, passw):
       self.password = generate_password_hash(passw)

   def __repr__(self):
      return '<User %r>' % self.username

   def is_authenticated(self):
      return self.is_authenticated

   def is_active(self):
      return True

   def is_anonymous(self):
      return False

   def get_id(self):
      return str(self.employee_id)

   @staticmethod
   def getById(id):
      employee = EmployeeService().get(id)
      print employee
      if (employee != None):
        employee.new = False
      return employee

   @staticmethod
   def getByCredential(username, passw):
      employee = EmployeeService().getByCredential(username, passw)
      print employee
      if (employee is not None):
        employee.new = False
      return employee

   @staticmethod
   def add(employee):
       service = EmployeeService()
       old_employee = service.getByUsername(employee.username)
       if (old_employee is not None):
          "throw exception user already exists"
          return False
       service.add(employee)
       return True

   @staticmethod
   def delete(employee):
       return EmployeeService().delete(employee)

   @staticmethod
   def update(employee):
      EmployeeService().update(employee)
