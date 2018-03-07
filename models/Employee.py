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
   service = EmployeeService()

   def __init__(self):
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
      employee = Employee.service.get(id)
      print employee
      if (employee != None):
        employee.new = False
      return employee

   @staticmethod
   def getAllExcluding(ids):
      employee = Employee.service.getAllByFilter(ids)
      print employee
      return employee

   @staticmethod
   def getAll():
      employee = Employee.service.getAll()
      print employee
      return employee

   @staticmethod
   def getByCredential(username, passw):
      employee = Employee.service.getByCredential(username, passw)
      print employee
      if (employee is not None):
        employee.new = False
      return employee

   @staticmethod
   def add(employee):

       old_employee = Employee.service.getByUsername(employee.username)
       if (old_employee is not None):
          "throw exception user already exists"
          return False
       Employee.service.add(employee)
       return True

   @staticmethod
   def delete(employee):
       return Employee.service.delete(employee)

   @staticmethod
   def update(employee):
      Employee.service.update(employee)
