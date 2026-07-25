from fastapi import FastAPI, HTTPException, status
from typing import List
from services.booking_storage_service import BookingStorageService
from api.schemas.booking_schema import BookingCreate, BookingResponse
from customers.customer import Customer
from services.booking_service import BookingService

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


@app.post(
    "/bookings",
    status_code=status.HTTP_201_CREATED,
    response_model=BookingResponse
)
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