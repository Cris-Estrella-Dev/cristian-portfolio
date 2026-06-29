from employees.employee import Employee

class RampAgent(Employee):

    def __init__(self, employee_id, first_name, last_name, email, base_airport,ramp_zone):
        super().__init__(employee_id, first_name, last_name, email, base_airport)
        self.__ramp_zone = ramp_zone

    def show_info(self):
        print("Role: Ramp Agent")
        print(f"Employee ID: {self.get_employee_id()}")
        print(f"Name: {self.get_full_name()}")
        print(f"Email: {self.get_email()}")
        print(f"Base Airport: {self.get_base_airport()}")
        print(f"Rampo Zone: {self.__ramp_zone}")

