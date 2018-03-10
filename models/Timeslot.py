from __future__ import print_function
from EmployeeSchedule import EmployeeSchedule
from datetime import datetime
from datetime import timedelta

class Timeslot:
    global start_time
    global end_time

    start_time = "09:00 AM"
    end_time = "05:00 PM"

    def __init__(self, start="", end="", avail=True):
        self.start = start
        self.end = end
        self.available = avail

    """
    length in minutes
    """
    @staticmethod
    def generateTimeslots(length, date):
        timeslots = []
        start = datetime.strptime(date+" "+start_time, "%d.%m.%Y %I:%M %p")
        end = datetime.strptime(date+" "+end_time, "%d.%m.%Y %I:%M %p")
        if datetime.now() > start or datetime.now() > end:
            return []
        current_start = start
        current_end = current_start + timedelta(minutes = int(length))
        while(current_end < end):
            slot = Timeslot(current_start, current_end)
            timeslots.append(slot)
            current_start = current_end
            current_end = current_start + timedelta(minutes = int(length))
        if end >= current_end:
            slot = Timeslot(current_start, current_end)
            timeslots.append(slot)
        return timeslots


    @staticmethod
    def getAvailableTimeslots(length, employee_id, date):
        start = datetime.strptime(date+" "+start_time, "%d.%m.%Y %I:%M %p")
        end = datetime.strptime(date+" "+end_time, "%d.%m.%Y %I:%M %p")
        schedules = EmployeeSchedule.getByTime(employee_id, start, end)
        timeslots = Timeslot.generateTimeslots(length, date)
        print(schedules)

        for schedule in schedules:
            print("--------------------")
            if schedule.available == "N":
                print(schedule.employee_schedule_id)
                for slot in timeslots :
                    if slot.start >= schedule.end_time:
                        break
                    else:
                        if ((schedule.start_time <= slot.start and schedule.end_time >= slot.start )
                            or (schedule.start_time <= slot.end and schedule.end_time >= slot.end)
                            or (slot.start <= schedule.start_time and slot.end >= schedule.start_time)
                            or (slot.start <= schedule.end_time and slot.end >= schedule.end_time)):
                            slot.available = False
        return timeslots
