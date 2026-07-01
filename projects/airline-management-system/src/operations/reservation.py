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
        print("Customer checked in successfully.")

    def cancel(self):
        self.__status = "Cancelled"
        print("Flight reservation cancelled successfully.")

    def add_bag(self, bag):
        self.__bags.append(bag)
        print("Bag added successfully.")

    def delete_bag(self, bag_id):
        for bag in self.__bags:
            if bag.get_bag_id() == bag_id:
                self.__bags.remove(bag)
                print("Bag deleted successfully.")
                return

        print("Bag not found.")

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
                