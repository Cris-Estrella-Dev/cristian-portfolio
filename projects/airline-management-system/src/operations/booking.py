class Booking:

    def __init__(self,booking_id, confirmation_number,customer,booking_date,status,total_price):
        self.__booking_id = booking_id
        self.__confirmation_number = confirmation_number
        self.__booking_date = booking_date
        self.__status = status
        self.__total_price = total_price
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
    
    def add_reservation(self,reservation):
        self.__reservations.append(reservation)
        print("Reservation has been added succesfully")

    def cancel_booking(self):
        self.__status = "Cancelled"
        for reservation in self.__reservations:
            reservation.cancel()
        print("Booking has been cancelled succesfully")

    def show_info(self):
        print(f"Booking ID: {self.get_booking_id()}")
        print(f"Confirmation Number: {self.get_confirmation_number()}")
        print(f"Booking date: {self.get_booking_date()}")
        print(f"Status: {self.get_status()}")
        print(f"Total Price: {self.get_total_price()}")
        print(f"Customer: {self.get_customer()}")
        print("---------------------------------\n")
        for reservation in self.__reservations:
            if not self.__reservations:
                print("There are no reservations associated to this booking")
            else:
                reservation.show_info()
    
    def get_status(self):
        return self.__status
    
    def get_total_price(self):
        return self.__total_price




    