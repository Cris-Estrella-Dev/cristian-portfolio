from fastapi import FastAPI, HTTPException, status
from typing import List
from services.booking_storage_service import BookingStorageService
from api.schemas.booking_schema import BookingCreate, BookingResponse, ReservationCreate
from customers.customer import Customer
from services.booking_service import BookingService
from operations.airport import Airport
from operations.flight import Flight


app = FastAPI(
    title="Airline Management System API",
    version="0.1.0",
    description="API for managing airline customers, bookings, reservations, flights, baggage, crew, and staff."
)


@app.get("/")
def root():
    return{"message": "Airline Management System API is running."}

@app.get("/health")
def health_check():
    return {
        "status": "ok"
    }


@app.get("/bookings", response_model=List[BookingResponse])
def list_bookings():
    storage_service = BookingStorageService()
    bookings = storage_service.load_bookings()
    return [booking.to_dict() for booking in bookings]



@app.get("/bookings/{confirmation_number}", response_model=BookingResponse)
def get_booking_by_confirmation_number(confirmation_number):
    storage_service = BookingStorageService()
    bookings = storage_service.load_bookings()

    for booking in bookings:
        if booking.get_confirmation_number() == confirmation_number.upper():
            return booking.to_dict()

    raise HTTPException(status_code=404,
        detail="Booking not found."
    )


@app.post("/bookings",status_code=status.HTTP_201_CREATED,response_model=BookingResponse)
def create_booking(booking_data: BookingCreate):
    try:
        customer = Customer(
            booking_data.customer.customer_id,
            booking_data.customer.first_name,
            booking_data.customer.last_name,
            booking_data.customer.email,
            booking_data.customer.phone_number
        )

        booking_service = BookingService()
        storage_service = BookingStorageService()

        new_booking = booking_service.create_booking(
            customer,
            booking_data.total_price
        )

        bookings = storage_service.load_bookings()
        bookings.append(new_booking)
        storage_service.save_bookings(bookings)

        return new_booking.to_dict()

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

@app.post("/bookings/{confirmation_number}/reservations",status_code=status.HTTP_201_CREATED,response_model=BookingResponse)
def add_reservation_to_booking(reservation_data: ReservationCreate, confirmation_number: str):

    try:
        storage_service = BookingStorageService()
        booking_service = BookingService()

        bookings = storage_service.load_bookings()

        booking_found = None

        for booking in bookings:
            if booking.get_confirmation_number() == confirmation_number.upper():
                booking_found = booking
                break

        if booking_found is None:
            raise HTTPException(
                status_code=404,
                detail="Booking not found."
            )

        origin_airport_data = reservation_data.flight.origin_airport

        origin_airport = Airport(
            origin_airport_data.airport_code,
            origin_airport_data.name,
            origin_airport_data.city,
            origin_airport_data.state,
            origin_airport_data.country
        )

        destination_airport_data = reservation_data.flight.destination_airport

        destination_airport = Airport(
            destination_airport_data.airport_code,
            destination_airport_data.name,
            destination_airport_data.city,
            destination_airport_data.state,
            destination_airport_data.country
        )

        flight_data = reservation_data.flight

        flight = Flight(
            flight_data.flight_number,
            origin_airport,
            destination_airport,
            flight_data.departure_time,
            flight_data.arrival_time,
            flight_data.status
        )

        reservation = booking_service.create_reservation(
            flight,
            reservation_data.status,
            reservation_data.fare_type,
            reservation_data.boarding_position,
            reservation_data.check_in_status
        )

        booking_service.add_reservation_to_booking(
            booking_found,
            reservation
        )

        storage_service.save_bookings(bookings)

        return booking_found.to_dict()

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )
