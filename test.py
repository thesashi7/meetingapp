from test.EmployeeTest import EmployeeTest
from test.AdministratorTest import AdministratorTest
from test.RoomTest import RoomTest
from test.MeetingTest import MeetingTest
from test.MeetingAttendeeTest import MeetingAttendeeTest
from test.EmployeeScheduleTest import EmployeeScheduleTest
from datetime import datetime
from datetime import timedelta

"""
Testing Employee

More to be added. Testing in it's infancy

"""
"""emTest = EmployeeTest()
emTest.run()

adminTest = AdministratorTest()
adminTest.run()
"""
# datetime_object = datetime.strptime('03.03.2018  12:50 AM', '%m.%d.%Y %I:%M %p')
# print datetime_object

test = MeetingTest()
test.run()
"""start_date = datetime.strptime("03.03.2018 01:49 PM", '%m.%d.%Y %I:%M %p')
print start_date
start_date = start_date - timedelta(minutes=1)
print start_date
print start_date.year"""
