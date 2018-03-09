from datetime import datetime

class Time:

    @staticmethod
    def convertToDateTime(date, time):
        return datetime.strptime(date+" "+time, '%m.%d.%Y %I:%M %p')
