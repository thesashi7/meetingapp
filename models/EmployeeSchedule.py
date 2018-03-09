from __future__ import print_function
from Model import Model
from services.EmployeeScheduleService import EmployeeScheduleService
from services.DatabaseService import DatabaseService

class EmployeeSchedule(Model):

   __tablename__ = 'employeeschedule'
   __table_args__ = {'autoload':True, 'autoload_with':DatabaseService.DBEngine()}
   service = EmployeeScheduleService()


   @staticmethod
   def isAvailable(emp_id, start, end):
       avail = True
       employee_schedules = EmployeeSchedule.service.getByTime(emp_id, start, end)
       if( (employee_schedules is None) or len(employee_schedules) == 0 ):
            avail = False
       else:
           for employee_schedule in employee_schedules:
               print(employee_schedule)
               print(employee_schedule.available)
               if employee_schedule.available == "N":
                   avail = False
                   break
       return avail

   @staticmethod
   def getByEmployeeScheduleId(id):
       employee_schedule= EmployeeSchedule.service.getByEmployeeScheduleId(id)
       return employee_schedule

   @staticmethod
   def getByEmployeeId(emp_id):
       employee_schedule= EmployeeSchedule.service.getByEmployeeId(emp_id)
       return employee_schedule

   @staticmethod
   def add(employee_schedule):
      EmployeeSchedule.service.add(employee_schedule)
      return True

   @staticmethod
   def delete(employee_schedule):
       return EmployeeSchedule.service.delete(employee_schedule)

   def update(self):
       EmployeeSchedule.service.update(self)
