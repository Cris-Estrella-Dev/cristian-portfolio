from operations.airport import Airport

class Flight:
    def __init__(self, flight_number, origin_airport, destination_airport, departure_time, arrival_time, status):
        self.__flight_number = flight_number
        self.__origin_airport = origin_airport
        self.__destination_airport = destination_airport
        self.__departure_time = departure_time
        self.__arrival_time = arrival_time
        self.__status = status

    def get_flight_number(self):
        return self.__flight_number

    def get_origin_airport(self):
        return self.__origin_airport

    def get_destination_airport(self):
        return self.__destination_airport

    def get_status(self):
        return self.__status

    def show_info(self):
        print(f"Flight Number: {self.__flight_number}")
        print(f"Origin Airport: {self.__origin_airport}")
        print(f"Destination Airport: {self.__destination_airport}")
        print(f"Departure Time: {self.__departure_time}")
        print(f"Arrival Time: {self.__arrival_time}")
        print(f"Status: {self.__status}")

    def __str__(self):
        return f"{self.__flight_number} | {self.__origin_airport} -> {self.__destination_airport}"
    

    def to_dict(self):

        return{
            "flight_number": self.__flight_number,
            "origin_airport": self.__origin_airport.to_dict(),
            "destination_airport": self.__destination_airport.to_dict(),
            "departure_time": self.__departure_time,
            "arrival_time": self.__arrival_time,
            "status": self.__status
        }
    

    def from_dict(data):
        origin_airport = Airport.from_dict(data["origin_airport"])
        destination_airport = Airport.from_dict(data["destination_airport"])
        return Flight(
            data["flight_number"],
            origin_airport,
            destination_airport,
            data["departure_time"],
            data["arrival_time"],
            data["status"]
        )
        
