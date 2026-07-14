import pytest

from operations.airport import Airport
from operations.flight import Flight
from operations.baggage import Baggage
from operations.reservation import Reservation




def create_sample_flight():
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

    return Flight(
        "WN476",
        lga,
        bna,
        "10:00 AM",
        "1:15 PM",
        "On time"
    )


def test_reservation_id_cannot_be_empty():
    flight = create_sample_flight()

    with pytest.raises(ValueError):
        Reservation(
            "",
            flight,
            "Confirmed",
            "WN-PLU",
            "4",
            "Checked-in"
        )


def test_reservation_flight_must_be_flight_object():
    with pytest.raises(ValueError):
        Reservation(
            "R001",
            "WN476",
            "Confirmed",
            "WN-PLU",
            "4",
            "Checked-in"
        )


def test_reservation_status_cannot_be_empty():
    flight = create_sample_flight()

    with pytest.raises(ValueError):
        Reservation(
            "R001",
            flight,
            "",
            "WN-PLU",
            "4",
            "Checked-in"
        )


def test_reservation_fare_type_cannot_be_empty():
    flight = create_sample_flight()

    with pytest.raises(ValueError):
        Reservation(
            "R001",
            flight,
            "Confirmed",
            "",
            "4",
            "Checked-in"
        )


def test_reservation_boarding_position_cannot_be_empty():
    flight = create_sample_flight()

    with pytest.raises(ValueError):
        Reservation(
            "R001",
            flight,
            "Confirmed",
            "WN-PLU",
            "",
            "Checked-in"
        )


def test_reservation_check_in_status_cannot_be_empty():
    flight = create_sample_flight()

    with pytest.raises(ValueError):
        Reservation(
            "R001",
            flight,
            "Confirmed",
            "WN-PLU",
            "4",
            ""
        )

def test_add_bag_must_receive_baggage_object():
    flight = create_sample_flight()

    reservation = Reservation(
        "R001",
        flight,
        "Confirmed",
        "WN-PLU",
        "4",
        "Checked-in"
    )

    with pytest.raises(ValueError):
        reservation.add_bag("034")


def test_reservation_cannot_add_duplicate_bag():
    flight = create_sample_flight()

    reservation = Reservation(
        "R001",
        flight,
        "Confirmed",
        "WN-PLU",
        "4",
        "Checked-in"
    )

    bag = Baggage(
        "034",
        "Red hard shell bag"
    )

    reservation.add_bag(bag)

    with pytest.raises(ValueError):
        reservation.add_bag(bag)



def test_reservation_to_dict_includes_nested_flight_and_bags():
    
    #Arranger
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

    flight = Flight(
        "WN476",
        lga,
        bna,
        "10:00 AM",
        "1:15 PM",
        "On time"

    )

    bag = Baggage(
        "034",
        "Red hard shell bag"
    )

    reservation = Reservation(
        "R001",
        flight,
        "Confirmed",
        "WN-PLU",
        "4",
        "Checked-in"
    )

    reservation.add_bag(bag)

    #Act
    result = reservation.to_dict()

    assert result["reservation_id"] == 'R001'
    assert result["flight"] == flight.to_dict()
    assert result["status"] == "Confirmed"
    assert result["fare_type"] == "WN-PLU"
    assert result["boarding_position"] == "4"
    assert result["check_in_status"] == "Checked-in"
    assert result["bags"] == [bag.to_dict()]



def test_reservation_from_dict_reconstructs_flight_and_baggage_objects():
    # Arrange
    reservation_data = {
        "reservation_id": "R001",
        "flight": {
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
        },
        "status": "Confirmed",
        "fare_type": "WN-PLU",
        "boarding_position": "4",
        "check_in_status": "Checked-in",
        "bags": [
            {
                "bag_id": "034",
                "bag_type": "Red hard shell bag"
            }
        ]
    }


    reservation = Reservation.from_dict(reservation_data)

    # Assert
    assert reservation.get_flight_reservation_id() == "R001"
    assert reservation.get_status() == "Confirmed"

    assert isinstance(reservation.get_flight(), Flight)
    assert reservation.get_flight().to_dict() == reservation_data["flight"]

    assert len(reservation.get_bags()) == 1
    assert isinstance(reservation.get_bags()[0], Baggage)
    assert reservation.get_bags()[0].to_dict() == reservation_data["bags"][0]


def test_reservation_serialization_round_trip():
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

    flight = Flight(
        "WN476",
        lga,
        bna,
        "10:00 AM",
        "1:15 PM",
        "On time"
    )

    bag = Baggage(
        "034",
        "Red hard shell bag"
    )

    original_reservation = Reservation(
        "R001",
        flight,
        "Confirmed",
        "WN-PLU",
        "4",
        "Checked-in"
    )

    original_reservation.add_bag(bag)

    # Act
    reservation_data = original_reservation.to_dict()
    reconstructed_reservation = Reservation.from_dict(reservation_data)

    # Assert
    assert reconstructed_reservation.to_dict() == original_reservation.to_dict()