from operations.airport import Airport
from operations.flight import Flight
from customers.customer import Customer
from services.booking_service import BookingService
from operations.reservation import Reservation
from operations.baggage import Baggage
from operations.booking import Booking

from employees.flight_attendant import FlightAttendant
from employees.ops_agent import OpsAgent
from employees.pilot import Pilot
from employees.ramp_agent import RampAgent

from operations.flight_staff_assignment import FlightStaffAssignment
from operations.flight_crew_assignment import FlightCrewAssignment

from services.booking_storage_service import BookingStorageService



# 1. Crear airports
lga = Airport("LGA", "LaGuardia Airport", "Queens - NYC", "NY", "USA")
bna = Airport("BNA", "Nashville International Airport", "Nashville", "TN", "USA")

# 2. Crear flight
flight = Flight("WN476", lga, bna, "10:00 AM", "1:15 PM", "On time")

# 3. Crear customer
customer = Customer("C001", "Nawel", "Tavares", "nawel@example.com", "809-702-3396")

customer2 = Customer("C002", "Cristian", "Estrella", "cristian@example.com", "225-459-5665")

# 4. Crear booking usando BookingService
booking_service = BookingService()

booking = booking_service.create_booking(customer, 230.00)
booking2 = booking_service.create_booking(customer2,500)

# 5. Crear reservation
reservation = Reservation(
    "R001",
    flight,
    "Confirmed",
    "WN-PLU",
    "4",
    "Checked-in"
)

reservation2 = Reservation(
    "R002",
    flight,
    "Confirmed",
    "WN-WGA",
    "8",
    "Checked-in"
)



# 6. Agregar baggage
bag1 = Baggage("034", "Red hard shell bag")
bag2 = Baggage("123", "blue soft shell bag")
reservation.add_bag(bag1)
reservation.add_bag(bag2)

# 7. Agregar reservation al booking
booking_service.add_reservation_to_booking(booking, reservation)
booking_service.add_reservation_to_booking(booking2,reservation2)

# 8. Crear pilots y flight attendants
pilot = Pilot("P001", "Edwin", "Estrella", "edwin@wnco.com", bna, "B334F")
flight_attendant = FlightAttendant("F001", "Allie", "Richards", "allie@wnco.com", bna, "Nashville")

# 9. Crear flight crew assignment
flight_crew_assignment = FlightCrewAssignment("023", flight)

flight_crew_assignment.add_pilot(pilot)
flight_crew_assignment.add_flight_attendant(flight_attendant)

# 10. Crear ops agent y ramp agents
ramp_agent = RampAgent("RA001", "Andre", "Taylor", "andre@wnco.com", lga, "Zone 25")
ops_agent = OpsAgent("OPS001", "Courtney", "Wright", "courtney@wnco.com", lga, "Gate 57")

# 11. Crear flight staff assignment
flight_staff_assignment = FlightStaffAssignment("004", flight)

flight_staff_assignment.add_ops_agent(ops_agent)
flight_staff_assignment.add_ramp_agent(ramp_agent)

# 12. Mostrar toda la información
print("\n========== BOOKING INFORMATION ==========")
booking.show_info()

print("\n========== RESERVATION INFORMATION ==========")
reservation.show_info()

print("\n========== FLIGHT CREW ASSIGNMENT ==========")
flight_crew_assignment.show_crew()

print("\n========== FLIGHT STAFF ASSIGNMENT ==========")
flight_staff_assignment.show_staff()


print("\n========== TESTING TO_DICT ==========")
booking_dict = booking.to_dict()
booking_dict2 = booking2.to_dict()
print(booking_dict)

print("\n========== TESTING FROM_DICT ==========")
reconstructed_booking = Booking.from_dict(booking_dict)
reconstructed_booking2 = Booking.from_dict(booking_dict2)

reconstructed_booking.show_info()
reconstructed_booking2.show_info()


storage_service = BookingStorageService()

print("\n========== BOOKING BEFORE SAVING ==========")
print(booking.to_dict())
bookings = storage_service.load_bookings()

bookings.append(booking)
bookings.append(booking2)

storage_service.save_bookings(bookings)
loaded_bookings = storage_service.load_bookings()

print("\n========== BOOKINGS LOADED FROM JSON ==========")
print(f"Collection type: {type(loaded_bookings)}")

for loaded_booking in loaded_bookings:
    print(f"Element type: {type(loaded_booking)}")
    loaded_booking.show_info()