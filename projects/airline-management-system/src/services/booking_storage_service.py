import json
import os

from operations.booking import Booking


class BookingStorageService:
    def __init__(self, file_path="data/bookings.json"):
        self.__file_path = file_path

    def save_bookings(self, bookings):
        bookings_data = [booking.to_dict() for booking in bookings]

        with open(self.__file_path, "w") as file:
            json.dump(bookings_data, file, indent=4)


    def load_bookings(self):
        if not os.path.exists(self.__file_path):
            return []

        with open(self.__file_path, "r") as file:
            file_content = file.read()

        if not file_content.strip():
            return []

        bookings_data = json.loads(file_content)

        return [Booking.from_dict(booking_data) for booking_data in bookings_data]

            