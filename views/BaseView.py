
class BaseView():

    def __init__(self):
        self.message = {}
        self.message['success'] = ""
        self.message['fail'] = ""

    def setFlashMessage(self, type, msg):
        self.message[type] = msg
