from datetime import datetime


class Time:
    @staticmethod
    def convertToDateTime(date, time):
        return datetime.strptime(date + " " + time, '%d.%m.%Y %I:%M %p')

    @staticmethod
    def convertHourToMilitary(hour, min):
        return datetime.datetime.strptime(str(hour) + ":" + str(min) + '%H:%M').strftime('%I:%M %p')
