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

        # admin stuff

    def render_admin_add_room(self):
        return render_template('admin_add_room.html', success=self.message['success'],
                               fail=self.message['fail'])

    def render_admin_add_emp(self):
        return render_template('admin_add_emp.html', success=self.message['success'],
                               fail=self.message['fail'])

    def render_admin_config_room(self, rooms):
        return render_template('admin_config_room.html', rooms=rooms)

    def render_admin_config_emp(self, employees):
        return render_template('admin_config_emp.html', employees=employees)

    def render_admin_login(self):
        form = LoginForm()
        return render_template('admin_login.html', form=form)

    def render_admin_setting(self, emp):
        return render_template('admin_setting.html', emp=emp, success=self.message['success'],
                               fail=self.message['fail'])
