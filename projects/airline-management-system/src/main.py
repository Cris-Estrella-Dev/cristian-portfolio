from employees.employee import Employee
from operations.flight import Flight
from employees.ops_agent import OpsAgent
from employees.ramp_agent import RampAgent
from operations.flight_staff_assignment import FlightStaffAssignment
from operations.airport import Airport



lga = Airport(

    "LGA",
    "LaGuardia Airport",
    "Queens, New York City",
    "New York",
    "USA"

)

flight = Flight(

    "WN2543",
    "LGA",
    "MDW",
    "10:00 AM",
    "12:00 PM",
    "On time"

)

ops_agent = OpsAgent(

    "e001",
    "Cristian",
    "Estrella",
    "cristian@example.com",
    lga,
    "54"

)

ramp_agent = RampAgent(

    "e002",
    "Nawel",
    "Taveras",
    "nawel@example.com",
    lga,
    "30B"

)

flight_staff_assignment = FlightStaffAssignment(

    "1234",
    flight
)

flight_staff_assignment.add_ramp_agent(ramp_agent)
flight_staff_assignment.add_ops_agent(ops_agent)

flight_staff_assignment.show_staff()