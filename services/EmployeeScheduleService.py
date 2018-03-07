from DatabaseService import DatabaseService


class EmployeeScheduleService(DatabaseService):
    def get(self, id, serialize=False):
        from models.EmployeeSchedule import EmployeeSchedule
        employee_schedule = None
        employee_schedule = self.session.query(EmployeeSchedule).get(id)
        if serialize:
            return employee_schedule.serialize()
        else:
            return employee_schedule

    def getByEmployeeId(self, emp_id):
        from models.EmployeeSchedule import EmployeeSchedule
        employee_schedule = self.session.query(EmployeeSchedule).filter(
            EmployeeSchedule.employee_id == str(emp_id)).all()
        if (len(employee_schedule) > 0):
            return employee_schedule
        return None

    def add(self, employee_schedule):
        from models.EmployeeSchedule import EmployeeSchedule
        if isinstance(employee_schedule, EmployeeSchedule):
            self.session.add(employee_schedule)
            self.session.commit()

    def delete(self, employee_schedule):
        from models.EmployeeSchedule import EmployeeSchedule
        if isinstance(employee_schedule, EmployeeSchedule):
            self.session.delete(employee_schedule)
            self.session.commit()

    def update(self, employee_schedule):
        from models.EmployeeSchedule import EmployeeSchedule
        if isinstance(employee_schedule, EmployeeSchedule):
            self.session.commit()
