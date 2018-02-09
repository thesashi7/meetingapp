from flask import render_template
from LoginForm import LoginForm
from CalendarView import CalendarView

class PageView():

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
