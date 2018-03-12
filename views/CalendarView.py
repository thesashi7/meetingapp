from flask import render_template


class CalendarView():
    def render(self):
        return render_template("calendar.html")
