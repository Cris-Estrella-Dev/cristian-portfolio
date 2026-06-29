from employees.employee import Employee

class Pilot(Employee):
    def __init__(self, employee_id, first_name, last_name, email, base_airport,pilot_license):
        super().__init__(employee_id, first_name, last_name, email, base_airport)
        self.__pilot_license = pilot_license

    def show_info(self):
        print("Role: Pilot")
        print(f"Employee ID: {self.get_employee_id()}")
        print(f"Name: {self.get_full_name()}")
        print(f"Email: {self.get_email()}")
        print(f"Base Airport: {self.get_base_airport()}")
        print(f"Pilot License: {self.__pilot_license}")


        
    