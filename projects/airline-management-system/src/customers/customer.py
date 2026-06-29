class Customer():

    def __init__(self,customer_id,first_name,last_name,email,phone_number):
        self._customer_id = customer_id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._phone_number = phone_number

    
    def get_full_name(self):
        return f"{self.__first_name} {self.__last_name}"


    def show_info(self):

        print(f"Customer ID: {self._customer_id}")
        print(f"Full name: {self.get_full_name()}")
        print(f"Email: {self._email}")
        print(f"Phone number: {self._phone_number}")

    


    