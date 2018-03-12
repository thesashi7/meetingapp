from __future__ import print_function
from flask import render_template
import calendar
from datetime import datetime
from datetime import timedelta

class CalendarView():

    def render(self, timeslots, date, events, type):
        next_date =  date + timedelta(days=1)
        prev_date = date - timedelta(days=1)
        #needed to get timeslots for the next and past day on the calendar
        base_start = datetime.strptime("01:00 AM", '%I:%M %p')
        template = "calendar.html"
        if type == 'p':
            template = "main_calendar.html"
        self.sortSchedules(events)
        return render_template(template, timeslots=timeslots, date=date, calendar=calendar, prev=prev_date, next=next_date,
            base_start = base_start, timedelta = timedelta, events = events)


    def sortSchedules(self, schedules):
        i = 0
        while (i<len(schedules)):
            j=i+1
            while(j<len(schedules)):
                print(str(schedules[i].start_time )+" > "+str(schedules[j].start_time))
                if(schedules[i].start_time > schedules[j].start_time):
                    schedules[i], schedules[j] = schedules[j], schedules[i]
                j+=1
            i+=1