from operations.flight import Flight
from operations.airport import Airport

def test_to_dict_includes_nested_airports():


    #Arrange
    lga = Airport(
        'LGA',
        'LaGuardia Airport',
        'Queens - NYC',
        'NY',
        'USA'
    )

    bna = Airport(
        'BNA',
        'Nashville International Airport',
        'Nashville',
        'TN',
        'USA'
    )

    flight = Flight(
        'WN476',
        lga,
        bna,
        '10:00 AM',
        '1:15 PM',
        'On time'
    )

    # Act
    result = flight.to_dict()

    # Assert
    assert result["flight_number"] == "WN476"
    assert result["origin_airport"] == lga.to_dict()
    assert result["destination_airport"] == bna.to_dict()
    assert result["departure_time"] == "10:00 AM"
    assert result["arrival_time"] == "1:15 PM"
    assert result["status"] == "On time"


def test_flight_from_dict_reconstructs_airport_objects():
    # Arrange
    flight_data = {
        "flight_number": "WN476",
        "origin_airport": {
            "airport_code": "LGA",
            "name": "LaGuardia Airport",
            "city": "Queens - NYC",
            "state": "NY",
            "country": "USA"
        },
        "destination_airport": {
            "airport_code": "BNA",
            "name": "Nashville International Airport",
            "city": "Nashville",
            "state": "TN",
            "country": "USA"
        },
        "departure_time": "10:00 AM",
        "arrival_time": "1:15 PM",
        "status": "On time"
    }

    # Act
    flight = Flight.from_dict(flight_data)

    # Assert
    assert flight.get_flight_number() == "WN476"

    assert isinstance(
        flight.get_origin_airport(),
        Airport
    )

    assert isinstance(
        flight.get_destination_airport(),
        Airport
    )

    assert flight.get_origin_airport().to_dict() == flight_data["origin_airport"]
    assert flight.get_destination_airport().to_dict() == flight_data["destination_airport"]
    assert flight.get_departure_time() == flight_data["departure_time"]
    assert flight.get_arrival_time() == flight_data["arrival_time"]


def test_flight_serialization_round_trip():
    # Arrange
    lga = Airport(
        "LGA",
        "LaGuardia Airport",
        "Queens - NYC",
        "NY",
        "USA"
    )

    bna = Airport(
        "BNA",
        "Nashville International Airport",
        "Nashville",
        "TN",
        "USA"
    )

    original_flight = Flight(
        "WN476",
        lga,
        bna,
        "10:00 AM",
        "1:15 PM",
        "On time"
    )

    # Act
    flight_data = original_flight.to_dict()
    reconstructed_flight = Flight.from_dict(flight_data)

    # Assert
    assert reconstructed_flight.to_dict() == original_flight.to_dict()