class Customer:
    def __init__(self, customer_id, first_name, last_name, email, phone_number):
        self.__customer_id = customer_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__phone_number = phone_number

    def get_customer_id(self):
        return self.__customer_id

    def get_full_name(self):
        return f"{self.__first_name} {self.__last_name}"

    def get_email(self):
        return self.__email

    def get_phone_number(self):
        return self.__phone_number

    def show_info(self):
        print(f"Customer ID: {self.__customer_id}")
        print(f"Full name: {self.get_full_name()}")
        print(f"Email: {self.__email}")
        print(f"Phone number: {self.__phone_number}")

    def __str__(self):
        return f"{self.__customer_id} - {self.get_full_name()}"