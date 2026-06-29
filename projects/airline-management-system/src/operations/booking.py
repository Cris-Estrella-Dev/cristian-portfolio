class Booking:

    def __init__(self,booking_id, confirmation_number,booking_date,status,total_price):
        self.__booking_id = booking_id
        self.__confirmation_number = confirmation_number
        self.__booking_date = booking_date
        self.__status = status
        self.__total_price = total_price

    def add_flight_reservation(self):
        pass

    def cancel_booking(self):
        pass

    def show_info(self):
        pass