from flask import render_template
from LoginForm import LoginForm
from BaseView import BaseView
from CalendarView import CalendarView


class PageView(BaseView):
    def render_landing(self):
        form = LoginForm()
        return render_template('login.html', form=form)

    def render_about(self):
        pass

    def render_contact(self):
        pass

    def render_calendar(self):
        c_view = CalendarView()
        return c_view.render()

    def render_schedule_add_emp(self, emp_list):
        return render_template('schedule.html', emp_l=emp_list)

    def render_schedule_add_room(self, room_list):
        return render_template('roomschedule.html', room_list=room_list)

    def render_meeting_confirm(self, result):
        return render_template('meetingconfirm.html', success=result)

    def render_dashboard(self, owned_m, pending_m, accepted_m):
        return render_template('dashboard.html', owned_m=owned_m, pending_m=pending_m, accepted_m=accepted_m)

    def render_employee_setting(self, emp):
        return render_template('employee/setting.html', emp=emp, success=self.message['success'],
                               fail=self.message['fail'])
