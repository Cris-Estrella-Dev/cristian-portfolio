from customers.customer import Customer
from operations.booking import Booking
from operations.reservation import Reservation
from operations.flight import Flight
from operations.baggage import Baggage
from operations.airport import Airport




origin_airport = Airport(

    "LGA",
    "LaGuardia Airport",
    "Queens - NYC",
    "NY",
    "USA"

)

destination_aiport = Airport(

    "MDW",
    "Chicago Midway International Airport",
    "Chicago",
    "IL",
    "USA"

)


flight  = Flight(

    "WN476",
    origin_airport,
    destination_aiport,
    "10:00 AM",
    "12:15 PM",
    "On Time"

)


customer = Customer(


    "C001",
    "Jureissi",
    "Tavarez",
    "jureissi@example.com",
    "809-702-3396"

)


booking = Booking(

    "B001",
    "BCOO2",
    customer,
    "07/01/2026",
    "Confirmed",
    "250$"

)



reservation = Reservation(

    "R001",
    flight,
    "Confirmed",
    "WNGA",
    "4",
    "Not checked-in"

)

baggage = Baggage(

    "BG001",
    "22R"


)




booking.add_reservation(reservation)


booking.show_info()