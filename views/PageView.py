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
