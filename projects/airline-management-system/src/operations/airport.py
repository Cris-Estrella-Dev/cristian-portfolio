class Airport:
    def __init__(self, airport_code, name, city, state, country):
        if not airport_code or not airport_code.strip():
            raise ValueError("Airport code cannot be empty.")

        if len(airport_code.strip()) != 3:
            raise ValueError("Airport code must have exactly 3 characters.")

        if not name or not name.strip():
            raise ValueError("Airport name cannot be empty.")

        if not city or not city.strip():
            raise ValueError("Airport city cannot be empty.")

        if not state or not state.strip():
            raise ValueError("Airport state cannot be empty.")

        if not country or not country.strip():
            raise ValueError("Airport country cannot be empty.")

        self.__airport_code = airport_code.strip().upper()
        self.__name = name.strip()
        self.__city = city.strip()
        self.__state = state.strip()
        self.__country = country.strip()
    

    def get_airport_code(self):
        return self.__airport_code

    def get_name(self):
        return self.__name
    
    def get_city(self):
        return self.__city
    
    def get_state(self):
        return self.__state

    def get_country(self):
        return self.__country

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