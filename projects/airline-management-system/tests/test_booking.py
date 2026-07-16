import pytest

from customers.customer import Customer
from operations.airport import Airport
from operations.flight import Flight
from operations.baggage import Baggage
from operations.reservation import Reservation
from operations.booking import Booking



def create_sample_customer():
    return Customer(
        "C001",
        "Nawel",
        "Tavares",
        "nawel@example.com",
        "809-702-3396"
    )


def create_sample_reservation():
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

    return reservation



def test_booking_id_cannot_be_empty():
    customer = create_sample_customer()

    with pytest.raises(ValueError):
        Booking(
            "",
            "ABC123",
            customer,
            "2026-07-05",
            "Active",
            230.00
        )


def test_booking_confirmation_number_cannot_be_empty():
    customer = create_sample_customer()

    with pytest.raises(ValueError):
        Booking(
            "BKG-123456",
            "",
            customer,
            "2026-07-05",
            "Active",
            230.00
        )


def test_booking_customer_must_be_customer_object():
    with pytest.raises(ValueError):
        Booking(
            "BKG-123456",
            "ABC123",
            "C001",
            "2026-07-05",
            "Active",
            230.00
        )


def test_booking_date_cannot_be_empty():
    customer = create_sample_customer()

    with pytest.raises(ValueError):
        Booking(
            "BKG-123456",
            "ABC123",
            customer,
            "",
            "Active",
            230.00
        )


def test_booking_status_cannot_be_empty():
    customer = create_sample_customer()

    with pytest.raises(ValueError):
        Booking(
            "BKG-123456",
            "ABC123",
            customer,
            "2026-07-05",
            "",
            230.00
        )


def test_booking_total_price_must_be_number():
    customer = create_sample_customer()

    with pytest.raises(ValueError):
        Booking(
            "BKG-123456",
            "ABC123",
            customer,
            "2026-07-05",
            "Active",
            "230"
        )


def test_booking_total_price_cannot_be_negative():
    customer = create_sample_customer()

    with pytest.raises(ValueError):
        Booking(
            "BKG-123456",
            "ABC123",
            customer,
            "2026-07-05",
            "Active",
            -230.00
        )


def test_booking_to_dict_includes_nested_customer_and_reservations():
    # Arrange
    customer = Customer(
        "C001",
        "Nawel",
        "Tavares",
        "nawel@example.com",
        "809-702-3396"
    )

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

    booking = Booking(
        "BKG-812523",
        "DRSSOW",
        customer,
        "2026-07-07",
        "Active",
        230.00
    )

    booking.add_reservation(reservation)

    # Act
    result = booking.to_dict()

    # Assert
    assert result["booking_id"] == "BKG-812523"
    assert result["confirmation_number"] == "DRSSOW"
    assert result["customer"] == customer.to_dict()
    assert result["booking_date"] == "2026-07-07"
    assert result["status"] == "Active"
    assert result["total_price"] == 230.00
    assert result["reservations"] == [reservation.to_dict()]





def test_booking_from_dict_reconstructs_customer_and_reservation_objects():
    # Arrange
    booking_data = {
        "booking_id": "BKG-123456",
        "confirmation_number": "ABC123",
        "customer": {
            "customer_id": "C001",
            "first_name": "Nawel",
            "last_name": "Tavares",
            "email": "nawel@example.com",
            "phone_number": "809-702-3396"
        },
        "booking_date": "2026-07-05",
        "status": "Active",
        "total_price": 230.00,
        "reservations": [
            {
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
        ]
    }

    # Act
    booking = Booking.from_dict(booking_data)

    # Assert
    assert booking.get_booking_id() == "BKG-123456"
    assert booking.get_confirmation_number() == "ABC123"
    assert booking.get_booking_date() == "2026-07-05"
    assert booking.get_status() == "Active"
    assert booking.get_total_price() == 230.00

    assert isinstance(booking.get_customer(), Customer)
    assert booking.get_customer().to_dict() == booking_data["customer"]

    assert len(booking.get_reservations()) == 1
    assert isinstance(booking.get_reservations()[0], Reservation)
    assert booking.get_reservations()[0].to_dict() == booking_data["reservations"][0]



def test_booking_serialization_round_trip():
    # Arrange
    customer = Customer(
        "C001",
        "Nawel",
        "Tavares",
        "nawel@example.com",
        "809-702-3396"
    )

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

    original_booking = Booking(
        "BKG-123456",
        "ABC123",
        customer,
        "2026-07-05",
        "Active",
        230.00
    )

    original_booking.add_reservation(reservation)

    # Act
    booking_data = original_booking.to_dict()
    reconstructed_booking = Booking.from_dict(booking_data)

    # Assert
    assert reconstructed_booking.to_dict() == original_booking.to_dict()


def test_add_reservation_must_receive_reservation_object():
    customer = create_sample_customer()

    booking = Booking(
        "BKG-123456",
        "ABC123",
        customer,
        "2026-07-05",
        "Active",
        230.00
    )

    with pytest.raises(ValueError):
        booking.add_reservation("R001")


def test_booking_cannot_add_duplicate_reservation():
    customer = create_sample_customer()
    reservation = create_sample_reservation()

    booking = Booking(
        "BKG-123456",
        "ABC123",
        customer,
        "2026-07-05",
        "Active",
        230.00
    )

    booking.add_reservation(reservation)

    with pytest.raises(ValueError):
        booking.add_reservation(reservation)