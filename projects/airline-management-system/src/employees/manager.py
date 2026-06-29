from employees.employee import Employee


class Manager(Employee):
    def __init__(self, employee_id, first_name, last_name, email, base_airport,department):
        super().__init__(employee_id, first_name, last_name, email, base_airport)
        self.__department = department

    def show_info(self):
        print("Role: Manager")
        print(f"Employee ID: {self.get_employee_id()}")
        print(f"Name: {self.get_full_name()}")
        print(f"Email: {self.get_email()}")
        print(f"Base Airport: {self.get_base_airport()}")
        print(f"Department: {self.__department}")
