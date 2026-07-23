from customers.customer import Customer
from operations.airport import Airport
from operations.flight import Flight
from operations.baggage import Baggage
from operations.reservation import Reservation
from operations.booking import Booking
from services.booking_storage_service import BookingStorageService


def create_sample_booking():
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
        "BKG-123456",
        "ABC123",
        customer,
        "2026-07-05",
        "Active",
        230.00
    )

    booking.add_reservation(reservation)

    return booking




def test_save_bookings_creates_json_file(tmp_path):
    # Arrange
    file_path = tmp_path / "bookings.json"
    storage_service = BookingStorageService(file_path)

    booking = create_sample_booking()

    # Act
    storage_service.save_bookings([booking])

    # Assert
    assert file_path.exists()


def test_save_and_load_bookings_round_trip(tmp_path):
    # Arrange
    file_path = tmp_path / "bookings.json"
    storage_service = BookingStorageService(file_path)

    original_booking = create_sample_booking()

    # Act
    storage_service.save_bookings([original_booking])
    loaded_bookings = storage_service.load_bookings()

    # Assert
    assert len(loaded_bookings) == 1

    loaded_booking = loaded_bookings[0]

    assert isinstance(loaded_booking, Booking)
    assert loaded_booking.to_dict() == original_booking.to_dict()


def test_load_bookings_returns_empty_list_when_file_does_not_exist(tmp_path):
    # Arrange
    file_path = tmp_path / "bookings.json"
    storage_service = BookingStorageService(file_path)

    # Act
    loaded_bookings = storage_service.load_bookings()

    # Assert
    assert loaded_bookings == []


def test_load_bookings_returns_empty_list_when_file_is_empty(tmp_path):
    file_path = tmp_path / "bookings.json"
    file_path.write_text("")

    storage_service = BookingStorageService(file_path)

    bookings = storage_service.load_bookings()

    assert bookings == []