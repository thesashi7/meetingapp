from DatabaseService import DatabaseService
from werkzeug.security import check_password_hash

class AdministratorService(DatabaseService):

   def get(self, id, serialize = False):
     from models.Administrator import Administrator
     admin = None
     admin = self.session.query(Administrator).get(id)
     if serialize:
        return admin.serialize()
     else:
        return admin

   def getById(self, admin_id):
     from models.Administrator import Administrator
     admin = None
     admin = self.session.query(Administrator).filter(Administrator.administrator_id == str(admin_id)).all()
     return admin

   def getByCredential(self, username, passw):
     from models.Administrator import Administrator
     admin = None
     admin = self.session.query(Administrator).filter(Administrator.username == str(username)).all()
     if(len(admin) > 0 and check_password_hash(admin[0].password, passw) == True):
         return admin[0]
     return None

   def getByUsername(self, username):
     from models.Administrator import Administrator
     admin = None
     admin = self.session.query(Administrator).filter(Administrator.username == str(username)).all()
     if (len(admin) > 0):
         return admin[0]
     return None

   def add(self, administrator):
     from models.Administrator import Administrator
     if isinstance(administrator, Administrator):
        self.session.add(administrator)
        return self.session.commit()

   def delete(self, administrator):
     from models.Administrator import Administrator
     if isinstance(administrator, Administrator):
        current_sessions = self.session.object_session(administrator)
        current_sessions.delete(administrator)
        return current_sessions.commit()

   def update(self, administrator):
      from models.Administrator import Administrator
      current_sessions = self.session.object_session(administrator)
      current_sessions.flush()
      return current_sessions.commit()
