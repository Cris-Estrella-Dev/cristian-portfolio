from employees.employee import Employee


class OpsAgent(Employee):

    def __init__(self, employee_id, first_name, last_name, email, base_airport,assigned_gate):
        super().__init__(employee_id, first_name, last_name, email, base_airport)
        self._assigned_gate = assigned_gate

    def show_info(self):
        print("Role: OpsAgent")
        print(f"Employee ID: {self.get_employee_id()}")
        print(f"Name: {self.get_full_name()}")
        print(f"Email: {self.get_email()}")
        print(f"Base Airport: {self.get_base_airport()}")
        print(f"Assigned gate: {self.__assigned_gate}")

    