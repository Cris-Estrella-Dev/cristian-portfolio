from employees.employee import Employee


class Supervisor(Employee):

    def __init__(self, employee_id, first_name, last_name, email, base_airport, team_name):
        super().__init__(employee_id, first_name, last_name, email, base_airport)
        self._team_name = team_name


    def show_info(self):
        print("Role: Supervisor")
        print(f"Employee ID: {self.get_employee_id()}")
        print(f"Name: {self.get_full_name()}")
        print(f"Email: {self.get_email()}")
        print(f"Base Airport: {self.get_base_airport()}")
        print(f"Team name: {self._team_name}")

        