from operations.airport import Airport
from operations.flight import Flight


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

flight = Flight(
    "WN123",
    lga,
    mdw,
    "08:30 AM",
    "10:15 AM",
    "On Time"
)

flight.show_info()