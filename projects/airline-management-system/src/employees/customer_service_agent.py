from employees.employee import Employee

class CustomerServiceAgent(Employee):

    def __init__(self, employee_id, first_name, last_name, email, base_airport, assigned_area):
        super().__init__(employee_id, first_name, last_name, email, base_airport)
        self.__assigned_area = assigned_area

    def show_info(self):
        print("Role: Customer Service Agent")
        print(f"Employee ID: {self.get_employee_id()}")
        print(f"Name: {self.get_full_name()}")
        print(f"Email: {self.get_email()}")
        print(f"Base Airport: {self.get_base_airport()}")
        print(f"Assigned Area: {self.__assigned_area}")