from Model import Model
from services.EmployeeScheduleService import EmployeeScheduleService
from services.DatabaseService import DatabaseService


class EmployeeSchedule(Model):
    __tablename__ = 'employeeschedule'
    __table_args__ = {'autoload': True, 'autoload_with': DatabaseService.DBEngine()}
    service = EmployeeScheduleService()

    @staticmethod
    def getByEmployeeScheduleId(id):
        employee_schedule = EmployeeSchedule.service.getByEmployeeScheduleId(id)
        return employee_schedule

    @staticmethod
    def getByEmployeeId(emp_id):
        employee_schedule = EmployeeSchedule.service.getByEmployeeId(emp_id)
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
