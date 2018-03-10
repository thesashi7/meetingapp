from DatabaseService import DatabaseService
from werkzeug.security import check_password_hash
from sqlalchemy import or_, and_

class EmployeeService(DatabaseService):

   def getAll(self):
     from models.Employee import Employee
     employee = None
     employee = self.session.query(Employee).all()
     return employee

   def getAllByFilter(self, emp_ids, visible='Y'):
     from models.Employee import Employee
     employees = None
     employees = self.session.query(Employee).filter(
     and_(~Employee.employee_id.in_(emp_ids), Employee.visible == str(visible))).all()
     return employees

   def get(self, id, serialize = False):
     from models.Employee import Employee
     employee = None
     employee = self.session.query(Employee).get(id)
     if serialize:
        return employee.serialize()
     else:
        return employee

   def getById(self, employee_id):
     from models.Employee import Employee
     employee = None
     employee = self.session.query(Employee).filter(Employee.employee_id == str(employee_id)).all()
     return employee

   def getByUsername(self, username):
     from models.Employee import Employee
     employee = None
     employee = self.session.query(Employee).filter(Employee.username == str(username)).all()
     if (len(employee) > 0):
         return employee[0]
     return None

   def getByCredential(self, username, passw):
     from models.Employee import Employee
     employee = None
     employee = self.session.query(Employee).filter(Employee.username == str(username)).all()
     if(len(employee) > 0 and check_password_hash(employee[0].password, passw) == True):
         return employee[0]
     return None

   def add(self, employee):
     from models.Employee import Employee
     if isinstance(employee, Employee):
        self.session.add(employee)
        return self.session.commit()

   def delete(self, employee):
     from models.Employee import Employee
     if isinstance(employee, Employee):
        self.session.delete(employee)
        self.session.commit()

   def update(self, employee):
      from models.Employee import Employee
      if isinstance(employee, Employee):
          self.session.commit()
