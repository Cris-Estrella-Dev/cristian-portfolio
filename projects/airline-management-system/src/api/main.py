from fastapi import FastAPI
from services.booking_storage_service import BookingStorageService

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


@app.get("/bookings")
def list_bookings():
    storage_service = BookingStorageService()
    bookings = storage_service.load_bookings()
    return [booking.to_dict() for booking in bookings]

