from models.Notification import Notification


class NotificationTest:
    def addNotification(self):
        notification = Notification()
        notification.employee_id = 10
        notification.message = "Fucc a"
        notification.active = "Y"
        print Notification.add(notification)

    def getNotification(self):
        notifications = Notification.getActiveByEmployeeId(10)
        print notifications
        for notification in notifications:
            if notification != None:
                print notification.employee_id
                print notification.message
                print notification.active

    def deleteNotification(self):
        notifications = Notification.getActiveByEmployeeId(10)
        print notifications
        for notification in notifications:
            if notification != None:
                Notification.delete(notification)

    def updateNotification(self):
        notifications = Notification.getActiveByEmployeeId(10)
        print notifications
        for notification in notifications:
            if notification != None:
                notification.message = "Sucka"
                notification.update()

    def run(self):
        # self.addNotification()
        self.getNotification()
        self.deleteNotification()
        # self.updateNotification()
