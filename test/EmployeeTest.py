from models.Employee import Employee

class EmployeeTest:

    def testAddEmployee(self):
       emp = Employee()
       emp.setCredentials("sam","hunt")
       print Employee.add(emp)

    def testGetEmployee(self):
       emp = Employee.getByCredential("sam", "hunt")
       print emp
       if emp!=None:
           print emp.username
           print emp.password
           print emp.employee_id


    def testDeleteEmployee(self):
       emp = Employee.getByCredential("sam", "hunt")
       print emp
       if emp!=None:
          print emp.username
          Employee.delete(emp)


    def run(self):
       self.testAddEmployee()
       #self.testGetEmployee()
       #self.testDeleteEmployee()
