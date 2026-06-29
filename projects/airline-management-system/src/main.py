from operations.airport import Airport
from operations.flight import Flight
from operations.flight_crew_assignment import FlightCrewAssignment

from employees.pilot import Pilot
from employees.flight_attendant import FlightAttendant


# Airports
lga = Airport(
    "LGA",
    "LaGuardia Airport",
    "New York",
    "NY",
    "USA"
)

mdw = Airport(
    "MDW",
    "Chicago Midway International Airport",
    "Chicago",
    "IL",
    "USA"
)

# Flight
flight = Flight(
    "WN123",
    lga,
    mdw,
    "08:30 AM",
    "10:15 AM",
    "On Time"
)

# Pilots
pilot1 = Pilot(
    "E001",
    "Carlos",
    "Martinez",
    "carlos@example.com",
    mdw,
    "PL-12345"
)

pilot2 = Pilot(
    "E002",
    "Ana",
    "Gomez",
    "ana@example.com",
    lga,
    "PL-67890"
)

# Flight attendants
flight_attendant1 = FlightAttendant(
    "E003",
    "Maria",
    "Lopez",
    "maria@example.com",
    lga,
    "LGA"
)

flight_attendant2 = FlightAttendant(
    "E004",
    "Jose",
    "Ramirez",
    "jose@example.com",
    mdw,
    "LGA"
)

# Crew assignment
crew_assignment = FlightCrewAssignment(
    "CA001",
    flight
)

crew_assignment.add_pilot(pilot1)
crew_assignment.add_pilot(pilot2)

crew_assignment.add_flight_attendant(flight_attendant1)
crew_assignment.add_flight_attendant(flight_attendant2)

print("\n--- Flight Crew Assignment ---")
crew_assignment.show_crew()