class Airport:
    def __init__(self, airport_code, name, city, state, country):
        self.__airport_code = airport_code
        self.__name = name
        self.__city = city
        self.__state = state
        self.__country = country

    def get_airport_code(self):
        return self.__airport_code

    def get_name(self):
        return self.__name

    def show_info(self):
        print(f"Airport Code: {self.__airport_code}")
        print(f"Name: {self.__name}")
        print(f"City: {self.__city}")
        print(f"State: {self.__state}")
        print(f"Country: {self.__country}")

    def __str__(self):
        return f"{self.__airport_code} - {self.__name}"
    
    def to_dict(self):
        return{
            "airport_code": self.__airport_code,
            "name": self.__name,
            "city": self.__city,
            "state": self.__state,
            "country": self.__country
        }
    
    @staticmethod
    def from_dict(data):
        return Airport(
            data["airport_code"],
            data["name"],
            data["city"],
            data["state"],
            data["country"]
        )