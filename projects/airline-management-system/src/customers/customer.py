class Customer():

    def __init__(self,customer_id,first_name,last_name,email,phone_number):
        self._customer_id = customer_id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._phone_number = phone_number

    def get_customer_id(self):
        return self._customer_id

    def get_full_name(self):
        return f"{self._first_name} {self._last_name}"
    
    def get_email(self):
        return self._email
    
    def get_phone_number(self):
        return self._phone_number
    
    
    def show_info(self):

        print(f"Customer ID: {self.get_customer_id()}")
        print(f"Full name: {self.get_full_name()}")
        print(f"Email: {self.get_email()}")
        print(f"Phone number: {self.get_phone_number()}")


    