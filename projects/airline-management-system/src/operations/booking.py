class Booking:

    def __init__(self,booking_id, confirmation_number,booking_date,status,total_price):
        self.__booking_id = booking_id
        self.__confirmation_number = confirmation_number
        self.__booking_date = booking_date
        self.__status = status
        self.__total_price = total_price


    def get_booking_id(self):
        return self.__booking_id
    
    def get_confirmation_number(self):
        return self.__confirmation_number
    
    def get_booking_date(self):
        return self.__booking_date
    
    def get_status(self):
        return self.__status
    
    def get_total_price(self):
        return self.__total_price

    def add_flight_reservation(self):
        pass

    def cancel_booking(self):
        pass

    def show_info(self):
        pass