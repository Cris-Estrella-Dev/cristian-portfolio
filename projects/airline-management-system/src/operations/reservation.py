from operations.flight import Flight
from operations.baggage import Baggage

class Reservation:
    def __init__(self, reservation_id, flight, status, fare_type, boarding_position, check_in_status):
        self.__reservation_id = reservation_id
        self.__flight = flight
        self.__status = status
        self.__fare_type = fare_type
        self.__boarding_position = boarding_position
        self.__check_in_status = check_in_status
        self.__bags = []

    def get_flight_reservation_id(self):
        return self.__reservation_id

    def get_flight(self):
        return self.__flight

    def get_status(self):
        return self.__status

    def get_bags(self):
        return self.__bags

    def check_in(self):
        self.__check_in_status = "Checked In"


    def cancel(self):
        self.__status = "Cancelled"


    def add_bag(self, bag):
        self.__bags.append(bag)
       

    def delete_bag(self, bag_id):
        for bag in self.__bags:
            if bag.get_bag_id() == bag_id:
                self.__bags.remove(bag)
                return True

        

    def show_info(self):
        print(f"Reservation ID: {self.__reservation_id}")
        print(f"Flight: {self.__flight}")
        print(f"Status: {self.__status}")
        print(f"Fare Type: {self.__fare_type}")
        print(f"Boarding Position: {self.__boarding_position}")
        print(f"Check-in Status: {self.__check_in_status}")

        if not self.__bags:
            print("Baggage: No bags assigned")
        else:
            print("Baggage:")
            for bag in self.__bags:
                print(f"{bag}")
                
    def to_dict(self):

        return{
            "reservation_id": self.__reservation_id,
            "flight": self.__flight.to_dict(),
            "status": self.__status,
            "fare_type": self.__fare_type,
            "boarding_position": self.__boarding_position,
            "check_in_status": self.__check_in_status,
            "bags": [bag.to_dict() for bag in self.__bags]
        }
    
    @staticmethod
    def from_dict(data):
        flight = Flight.from_dict(data["flight"])

        bags = [
            Baggage.from_dict(bag_data)
            for bag_data in data["bags"]
        ]

        reservation = Reservation(
            data["reservation_id"],
            flight,
            data["status"],
            data["fare_type"],
            data["boarding_position"],
            data["check_in_status"]
        )

        for bag in bags:
            reservation.add_bag(bag)

        return reservation