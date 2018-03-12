from __future__ import print_function
from Model import Model
from services.EmployeeScheduleService import EmployeeScheduleService
from services.DatabaseService import DatabaseService
from datetime import datetime


class EmployeeSchedule(Model):
    __tablename__ = 'employeeschedule'
    __table_args__ = {'autoload': True, 'autoload_with': DatabaseService.DBEngine()}
    service = EmployeeScheduleService()
    global start_time
    global end_time

    start_time = "09:00 AM"
    end_time = "05:00 PM"

    @staticmethod
    def isAvailable(emp_id, start, end):
        avail = True
        date = str(start.month) + "." + str(start.day) + "." + str(start.year)
        print(date + " " + start_time)
        hr_start = datetime.strptime(date + " " + start_time, "%m.%d.%Y %I:%M %p")
        hr_end = datetime.strptime(date + " " + end_time, "%m.%d.%Y %I:%M %p")
        print(str(hr_start) + " ? " + str(start))
        print(str(hr_end) + " ? " + str(end))
        employee_schedules = EmployeeSchedule.service.getByTime(emp_id, start, end)
        if ((hr_start <= start and hr_end >= end) == False):
            avail = False
            print("ffffaallllse fucer")
        else:
            for employee_schedule in employee_schedules:
                print(employee_schedule)
                print(employee_schedule.available)
                if employee_schedule.available == "N":
                    avail = False
                    break
        return avail

    @staticmethod
    def getByMeetingId(meeting_id):
        employee_schedules = EmployeeSchedule.service.getByMeetingId(meeting_id)
        return employee_schedules

    @staticmethod
    def getByTime(emp_id, start, end):
        employee_schedules = EmployeeSchedule.service.getByTime(emp_id, start, end)
        return employee_schedules

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
