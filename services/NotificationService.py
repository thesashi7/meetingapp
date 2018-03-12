from DatabaseService import DatabaseService
from sqlalchemy import or_, and_


class NotificationService(DatabaseService):
    def getAll(self):
        from models.Notification import Notification
        notifications = None
        notifications = self.session.query(Notification).all()
        return notifications

    def get(self, id, serialize=False):
        from models.Notification import Notification
        notification = None
        notification = self.session.query(Notification).get(id)
        if serialize:
            return notification.serialize()
        else:
            return notification

    def getById(self, notification_id):
        return self.get(notification_id)

    def getByMeetingId(self, meeting_id):
        from models.Notification import Notification
        notifications = None
        notifications = self.session.query(Notification).filter(Notification.meeting_id == str(meeting_id)).all()
        return notifications

    def getActiveByEmployeeId(self, emp_id):
        from models.Notification import Notification
        notification = None
        notification = self.session.query(Notification).filter(
                and_(Notification.active == "Y", Notification.employee_id == str(emp_id))).all()
        return notification

    def add(self, notification):
        from models.Notification import Notification
        if isinstance(notification, Notification):
            self.session.add(notification)
            self.session.commit()

    def delete(self, notification):
        from models.Notification import Notification
        if isinstance(notification, Notification):
            self.session.delete(notification)
            self.session.commit()

    def update(self, notification):
        from models.Notification import Notification
        if isinstance(notification, Notification):
            self.session.commit()
