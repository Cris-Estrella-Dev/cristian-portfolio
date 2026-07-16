from customers.customer import Customer
from operations.reservation import Reservation

class Booking:

    def __init__(self, booking_id, confirmation_number, customer, booking_date, status, total_price):
        if not booking_id or not booking_id.strip():
            raise ValueError("Booking ID cannot be empty.")

        if not confirmation_number or not confirmation_number.strip():
            raise ValueError("Confirmation number cannot be empty.")

        if not isinstance(customer, Customer):
            raise ValueError("Customer must be a Customer object.")

        if not booking_date or not booking_date.strip():
            raise ValueError("Booking date cannot be empty.")

        if not status or not status.strip():
            raise ValueError("Booking status cannot be empty.")

        if not isinstance(total_price, (int, float)):
            raise ValueError("Total price must be a number.")

        if total_price < 0:
            raise ValueError("Total price cannot be negative.")

        self.__booking_id = booking_id.strip()
        self.__confirmation_number = confirmation_number.strip().upper()
        self.__booking_date = booking_date.strip()
        self.__status = status.strip()
        self.__total_price = float(total_price)
        self.__customer = customer
        self.__reservations = []


    def get_booking_id(self):
        return self.__booking_id
    
    def get_confirmation_number(self):
        return self.__confirmation_number
    
    def get_booking_date(self):
        return self.__booking_date
    
    def get_customer(self):
        return self.__customer
    
    def get_reservations(self):
        return self.__reservations
    
    def add_reservation(self, reservation):
        if not isinstance(reservation, Reservation):
            raise ValueError("Reservation must be a Reservation object.")

        for existing_reservation in self.__reservations:
            if existing_reservation.get_flight_reservation_id() == reservation.get_flight_reservation_id():
                raise ValueError("Reservation already exists in this booking.")

        self.__reservations.append(reservation)
    

    def cancel_booking(self):
        self.__status = "Cancelled"
        for reservation in self.__reservations:
            reservation.cancel()


    def show_info(self):
        print("-------------Booking-------------\n")
        print(f"Customer: {self.get_customer()}")
        print(f"Booking ID: {self.get_booking_id()}")
        print(f"Confirmation Number: {self.get_confirmation_number()}")
        print(f"Booking date: {self.get_booking_date()}")
        print(f"Status: {self.get_status()}")
        print(f"Total Price: {self.get_total_price():.2f}")
        print("-----------Reservation-------------\n")
        if not self.__reservations:
            print("There are no reservations associated with this booking")
            print("---------------------------------\n")
        else:
            for reservation in self.__reservations:
                reservation.show_info()
                print("---------------------------------\n")
        
    
    def get_status(self):
        return self.__status
    
    def get_total_price(self):
        return self.__total_price
    
    def to_dict(self):
        
        return{
            "booking_id": self.__booking_id,
            "confirmation_number": self.__confirmation_number,
            "customer": self.__customer.to_dict(),
            "booking_date": self.__booking_date,
            "status": self.__status,
            "total_price": self.__total_price,
            "reservations": [
            reservation.to_dict()
            for reservation in self.__reservations
        ]
        }
    
    @staticmethod
    def from_dict(data):

        customer = Customer.from_dict(data["customer"])

        booking = Booking(

            data["booking_id"],
            data["confirmation_number"],
            customer,
            data["booking_date"],
            data["status"],
            data["total_price"]
        )
        
    
        reservations = [Reservation.from_dict(reservation_data) for reservation_data in data["reservations"]]   

        for reservation in reservations:
            booking.add_reservation(reservation)

        return booking


    