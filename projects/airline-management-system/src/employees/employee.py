from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, employee_id, first_name, last_name, email, base_airport):
        self.__employee_id = employee_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__base_airport = base_airport

    def get_employee_id(self):
        return self.__employee_id

    def get_full_name(self):
        return f"{self.__first_name} {self.__last_name}"

    def get_email(self):
        return self.__email

    def get_base_airport(self):
        return self.__base_airport

    @abstractmethod
    def show_info(self):
        pass


