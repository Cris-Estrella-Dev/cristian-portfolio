from employees.employee import Employee


class FlightAttendant(Employee):
    def __init__(self, employee_id, first_name, last_name, email, base_airport,crew_base):
        super().__init__(employee_id, first_name, last_name, email, base_airport)
        self.__crew_base = crew_base

    def show_info(self):

        print("Role: Flight Attendant")
        print(f"Employee ID: {self.get_employee_id()}")
        print(f"Name: {self.get_full_name()}")
        print(f"Email: {self.get_email()}")
        print(f"Base Airport: {self.get_base_airport()}")
        print(f"Crew Base: {self.__crew_base}")

    