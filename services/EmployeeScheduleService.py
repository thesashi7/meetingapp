from __future__ import print_function
from DatabaseService import DatabaseService
from sqlalchemy import or_, and_
from datetime import timedelta

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

   def getByEmployeeScheduleId(self, emp_sc_id):
       return self.get(emp_sc_id)

   def getByMeetingId(self, meeting_id):
     from models.EmployeeSchedule import EmployeeSchedule
     employee_schedules = self.session.query(EmployeeSchedule).filter(EmployeeSchedule.meeting_id == str(meeting_id)).all()
     return employee_schedules

   def getByTime(self, emp_id, start, end):
       from models.EmployeeSchedule import EmployeeSchedule
       print ("====>"+str(emp_id))
       start = start + timedelta(minutes = 1)
       end = end - timedelta(minutes = 1)
       print (str(start)+" "+str(end))
       employee_schedules = None
       employee_schedules = self.session.query(EmployeeSchedule).filter(
         and_(
         or_(
          and_(EmployeeSchedule.start_time <= start, EmployeeSchedule.end_time >= start),
          and_(EmployeeSchedule.start_time <= end, EmployeeSchedule.end_time >= end),
          and_(start <= EmployeeSchedule.start_time, end >= EmployeeSchedule.start_time),
          and_(start <= EmployeeSchedule.end_time, end >= EmployeeSchedule.end_time)

          ), EmployeeSchedule.employee_id == str(emp_id))).all()
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
