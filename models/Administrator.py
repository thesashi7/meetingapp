from sqlalchemy.orm import relationship
from Model import Model
from services.AdministratorService import AdministratorService
from services.DatabaseService import DatabaseService
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Administrator(Model, UserMixin):
    __tablename__ = 'administrator'
    __table_args__ = {'autoload': True, 'autoload_with': DatabaseService.DBEngine()}
    service = AdministratorService()

    def __init__(self):
        self.is_authenticated = True
        self.type = "Admin"

    def is_authenticated(self):
        return self.is_authenticated

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.administrator_id)

    def setCredentials(self, username, passw):
        self.username = username
        self.setPassword(passw)

    def setPassword(self, passw):
        self.password = generate_password_hash(passw)

    @staticmethod
    def getById(id):
        admin = Administrator.service.get(id)
        print admin
        if (admin != None):
            admin.new = False
        return admin

    @staticmethod
    def getByUsername(username):
        admin = Administrator.service.getByUsername(username)
        print admin
        if (admin != None):
            admin.new = False
        return admin

    @staticmethod
    def getByCredential(username, passw):
        admin = Administrator.service.getByCredential(username, passw)
        print admin
        if (admin != None):
            admin.new = False
        return admin

    @staticmethod
    def add(administrator):
        old_admin = Administrator.service.getByUsername(administrator.username)
        if (old_admin is not None):
            "throw exception user already exists"
            return False
        Administrator.service.add(administrator)
        return True

    @staticmethod
    def delete(administrator):
        return Administrator.service.delete(administrator)

    def update(self):
        Administrator.service.update(self)
