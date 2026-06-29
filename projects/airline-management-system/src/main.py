from operations.airport import Airport
from employees.customer_service_agent import CustomerServiceAgent
from employees.flight_attendant import FlightAttendant
from employees.manager import Manager
from employees.ops_agent import OpsAgent



lga = Airport(
    "LGA",
    "LaGuardia Airport",
    "New York",
    "NY",
    "USA"
)

dal = Airport(
    "DAL",
    "Dallas Love Field Airport",
    "Dallas",
    "TX",
    "USA"
)

mdw = Airport(
    "MDW",
    "Chicago Midway international airport",
    "Chicago",
    "IL",
    "USA"
)

bna = Airport(
    "BNA",
    "Nashville International Airport",
    "Nashville",
    "TN",
    "USA"
)


csa = CustomerServiceAgent(
    "E001",
    "Cristian",
    "Estrella",
    "cristian@example.com",
    lga,
    "Ticket Counter"
)

fligh_attendant = FlightAttendant(
    "E002",
    "Nawel",
    "Taveras",
    "nawel@example.com",
    dal,
    "Dal"
)

    
    
manager = Manager(
    "E003",
    "Dario",
    "Di Giacomo",
    "dario@example.com",
    mdw,
    "Station manager"
)


ops_agent = OpsAgent(

    "E004",
    "Nicole",
    "Estrella",
    "nicole@example.com",
    bna,
    "57"
)



ops_agent.show_info()