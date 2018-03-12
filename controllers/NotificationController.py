from flask_login import current_user
from BaseController import BaseController
from models.Notification import Notification
import json


class NotificationController(BaseController):
    def get(self):
        # return all the notifications for the current logged in user
        # return json
        notifications = Notification.getActiveByEmployeeId(current_user.employee_id)
        json_not = list()
        for notif in notifications:
            json_not.append(notif.toDict())
        return json.dumps(json_not)

    def update(self, id):
        notification = Notification.getById(id)
        notification.active = "N"
        notification.update()
        return "Update"
