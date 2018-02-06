from DatabaseService import DatabaseService
from werkzeug.security import check_password_hash

class EmployeeService(DatabaseService):

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
        current_sessions = self.session.object_session(employee)
        current_sessions.delete(employee)
        return current_sessions.commit()
