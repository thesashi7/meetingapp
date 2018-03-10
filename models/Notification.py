from __future__ import print_function
from models.Model import Model
from services.NotificationService import NotificationService
from services.DatabaseService import DatabaseService
import json

class Notification(Model):

    #id, msg, active, employee_id
   __tablename__ = 'notification'
   __table_args__ = {'autoload':True, 'autoload_with':DatabaseService.DBEngine()}
   service = NotificationService()


   def update(self):
       Notification.service.update(self)

   def toJson(self):
       data = self.toDict()
       return json.dumps(data)

   def toDict(self):
       data = {
                "id":self.notification_id,
                "employee_id":self.employee_id,
                "message":self.message,
                "active": self.active,
                "meeting_id":self.meeting_id
       }
       return data
   @staticmethod
   def getById(not_id):
       notification = Notification.service.get(not_id)
       return notification

   @staticmethod
   def getByMeetingId(meeting_id):
       notifications = Notification.service.getByMeetingId(meeting_id)
       return notifications

   @staticmethod
   def getActiveByEmployeeId(emp_id):
       notification = Notification.service.getActiveByEmployeeId(emp_id)
       return notification

   @staticmethod
   def add(notification):
      Notification.service.add(notification)
      return True

   @staticmethod
   def delete(notification):
       return Notification.service.delete(notification)
