from Model import Model
from sqlalchemy.orm import relationship
from Model import Model
from services.AdministratorService import AdministratorService
from services.DatabaseService import DatabaseService
from werkzeug.security import generate_password_hash, check_password_hash

class Administrator(Model):
   __tablename__ = 'administrator'
   __table_args__ = {'autoload':True, 'autoload_with':DatabaseService.DBEngine()}

   def setCredentials(self, username, passw):
       self.username = username
       self.setPassword(passw)

   def setPassword(self, passw):
       self.password = generate_password_hash(passw)

   @staticmethod
   def getById(id):
      admin = AdministratorService().get(id)
      print admin
      if (admin != None):
        admin.new = False
      return admin

   @staticmethod
   def getByCredential(username, passw):
      admin = AdministratorService().getByCredential(username, passw)
      print admin
      if (admin != None):
        admin.new = False
      return admin

   @staticmethod
   def add(administrator):
       return AdministratorService().add(administrator)

   @staticmethod
   def delete(administrator):
       return AdministratorService().delete(administrator)
