from models.Administrator import Administrator

class AdministratorTest:

    def addAdministrator(self):
       admin = Administrator()
       admin.setCredentials("samy","hunt")
       print Administrator.add(admin)

    def getAdminstrator(self):
       admin = Administrator.getByCredential("samy", "hunt")
       print admin
       if admin!=None:
           print admin.username
           print admin.password
           print admin.administrator_id

    def deleteAdministrator(self):
       admin = Administrator.getByCredential("samy", "hunt")
       print admin
       if admin!=None:
          print admin.username
          Administrator.delete(admin)

    def updateAdministrator(self):
       admin = Administrator.getByCredential("ali", "champ")
       admin.setPassword("hunt")
       Administrator.update(admin)

    def run(self):
       self.updateAdministrator()
       #self.addAdministrator()
       #self.getAdminstrator()
       #self.deleteAdministrator()
