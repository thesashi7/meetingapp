from DatabaseService import DatabaseService
from sqlalchemy import or_, and_

class EmployeeScheduleService(DatabaseService):

   def get(self, id, serialize = False):
     from models.EmployeeSchedule import EmployeeSchedule
     employee_schedule = None
     employee_schedule = self.session.query(EmployeeSchedule).get(id)
     if serialize:
        return employee_schedule.serialize()
     else:
        return employee_schedule

   def getByEmployeeId(self, emp_id):
     from models.EmployeeSchedule import EmployeeSchedule
     employee_schedule= self.session.query(EmployeeSchedule).filter(EmployeeSchedule.employee_id == str(emp_id)).all()
     if(len(employee_schedule)>0):
        return employee_schedule
     return None

   def getByTime(self, emp_id, start, end):
       from models.EmployeeSchedule import EmployeeSchedule
       employee_schedules = None
       employee_schedules = self.session.query(EmployeeSchedule).filter(
         and_(
         or_(
          and_(EmployeeSchedule.start_time <= start, EmployeeSchedule.end_time >= start),
          and_(EmployeeSchedule.start_time <= end, EmployeeSchedule.end_time >= end))
          ), EmployeeSchedule.employee_id == emp_id).all()
       return employee_schedules

   def add(self, employee_schedule):
     from models.EmployeeSchedule import EmployeeSchedule
     if isinstance(employee_schedule, EmployeeSchedule):
        self.session.add(employee_schedule)
        self.session.commit()

   def delete(self, employee_schedule):
     from models.EmployeeSchedule import EmployeeSchedule
     if isinstance(employee_schedule, EmployeeSchedule):
        self.session.delete(employee_schedule)
        self.session.commit()


   def update(self, employee_schedule):
      from models.EmployeeSchedule import EmployeeSchedule
      if isinstance(employee_schedule, EmployeeSchedule):
          self.session.commit()
