from flask import render_template
from LoginForm import LoginForm
from BaseView import BaseView
from CalendarView import CalendarView
import calendar
from datetime import datetime
from datetime import timedelta

class EmployeeView(BaseView):

    def render_calendar(self):
       c_view = CalendarView()
       return c_view.render()

    def render_schedule_add_emp(self, emp_list):
        return render_template('schedule.html', emp_l = emp_list)

    def render_schedule_add_room(self, room_list):
        return render_template('roomschedule.html', room_list = room_list)

    def render_schedule_calendar(self, timeslots, date, length):
        next_date =  date + timedelta(days=1)
        prev_date = date - timedelta(days=1)
        #needed to get timeslots for the next and past day on the calendar
        base_start = datetime.strptime("01:00 AM", '%I:%M %p')
        base_end = base_start + timedelta(minutes=length)
        return render_template('schedulecalendar.html', timeslots=timeslots, date=date, calendar=calendar, prev=prev_date, next=next_date,
            base_start = base_start, base_end = base_end)

    def render_meeting_confirm(self, result):
        return render_template('meetingconfirm.html', success=result)

    def render_dashboard(self, owned_m, pending_m, accepted_m, meet_att_map):
        return render_template('dashboard.html', owned_m=owned_m, pending_m=pending_m, accepted_m=accepted_m, meet_att_map=meet_att_map, timedelta=timedelta)

    def render_employee_setting(self, emp):
        return render_template('employee/setting.html', emp=emp, success=self.message['success'],
        fail=self.message['fail'])
