from models.Employee import Employee

class EmployeeTest:

    def addEmployee(self):
       emp = Employee()
       emp.setCredentials("sam","hunt")
       print Employee.add(emp)

    def getEmployee(self):
       emp = Employee.getByCredential("sam", "hunt")
       print emp
       if emp!=None:
           print emp.username
           print emp.password
           print emp.employee_id


    def deleteEmployee(self):
       emp = Employee.getByCredential("sam", "hunt")
       print emp
       if emp!=None:
          print emp.username
          Employee.delete(emp)


    def run(self):
       self.addEmployee()
       #self.getEmployee()
       #self.deleteEmployee()
