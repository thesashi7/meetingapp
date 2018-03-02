from models.EmployeeSchedule import EmployeeSchedule

class EmployeeScheduleTest:

    def addEmployeeSchedule(self):
       employee_schedule = EmployeeSchedule()
       employee_schedule.employee_id = 10
       employee_schedule.start_time = "2018-11-03 01:00:00"
       employee_schedule.end_time = "2018-11-05 01:00:00"
       employee_schedule.available = "N"
       print EmployeeSchedule.add(employee_schedule)

    def getEmployeeSchedule(self):
       employee_schedule = EmployeeSchedule.getByEmployeeId(10)
       print employee_schedule
       if employee_schedule!=None:
           for em_s in employee_schedule:
               print em_s.employee_schedule_id


    def deleteEmployeeSchedule(self):
       employee_schedule = EmployeeSchedule.getByEmployeeId(10)
       print employee_schedule
       if employee_schedule!=None:
          for em_s in employee_schedule:
              print em_s.employee_schedule_id
              EmployeeSchedule.delete(em_s)

    def updateEmployeeSchedule(self):
       employee_schedule = EmployeeSchedule.getByEmployeeId(10)
       print employee_schedule
       employee_schedule.end_time = "2018-11-15 01:00:00"
       employee_schedule.update()

    def run(self):
       self.addEmployeeSchedule()
       self.getEmployeeSchedule()
       self.deleteEmployeeSchedule()
       #self.updateEmployeeSchedule()
