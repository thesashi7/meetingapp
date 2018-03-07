from models.Employee import Employee

class EmployeeTest:

    def addEmployee(self):
       emp = Employee()
       emp.setCredentials("sashi","thapaliya")
       print Employee.add(emp)

    def getAll(self):
        emp = Employee.getAll()
        print emp
        for e in emp:
            print e.username

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

    def updateEmployee(self):
       emp = Employee.getByCredential("saam", "hunt")
       emp.username = "sam"
       Employee.update(emp)

    def run(self):
        self.getAll()
       #self.addEmployee()
       #self.getEmployee()
       #self.deleteEmployee()
       #self.updateEmployee()
