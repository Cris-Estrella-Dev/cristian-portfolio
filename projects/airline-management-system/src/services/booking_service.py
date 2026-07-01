from datetime import datetime
import random
import string

from operations.booking import Booking


class BookingService:
    def create_booking(self, customer, total_price):
        booking_id = self.__generate_booking_id()
        confirmation_number = self.__generate_confirmation_number()
        booking_date = datetime.now().strftime("%Y-%m-%d")
        status = "Active"

        return Booking(
            booking_id,
            confirmation_number,
            customer,
            booking_date,
            status,
            total_price
        )

    def add_reservation_to_booking(self, booking, reservation):
        booking.add_reservation(reservation)
        print("Reservation added to booking successfully.")

    def cancel_booking(self, booking):
        booking.cancel_booking()

    def __generate_booking_id(self):
        return "BKG-" + "".join(random.choice(string.digits) for _ in range(6))

    def __generate_confirmation_number(self):
        characters = string.ascii_uppercase + string.digits
        return "".join(random.choice(characters) for _ in range(6))
    
    