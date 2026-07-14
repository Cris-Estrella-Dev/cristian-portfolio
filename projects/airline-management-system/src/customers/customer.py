class Customer:
    def __init__(self, customer_id, first_name, last_name, email, phone_number):
        
        if not customer_id or not customer_id.strip():
            raise ValueError("Customer ID cannot be empty")
        if not first_name or not first_name.strip():
            raise ValueError("Customer first name cannot be empty")
        if not last_name or not last_name.strip():
            raise ValueError("Customer last name cannot be empty")
        if not email or not email.strip():
            raise ValueError("Customer email cannot be empty")
        if not phone_number or not phone_number.strip():
            raise ValueError("Customer phone number cannot be empty")





        self.__customer_id = customer_id.strip().upper()
        self.__first_name = first_name.strip()
        self.__last_name = last_name.strip()
        self.__email = email.strip()
        self.__phone_number = phone_number.strip()

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
    
    def to_dict(self):
        return {
        "customer_id": self.__customer_id,
        "first_name": self.__first_name,
        "last_name": self.__last_name,
        "email": self.__email,
        "phone_number": self.__phone_number
    }

    @staticmethod
    def from_dict(data):
        return Customer(
            data["customer_id"],
            data["first_name"],
            data["last_name"],
            data["email"],
            data["phone_number"]
        )

    
    