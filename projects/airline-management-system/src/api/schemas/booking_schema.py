from typing import List

from pydantic import BaseModel


class CustomerCreate(BaseModel):
    customer_id: str
    first_name: str
    last_name: str
    email: str
    phone_number: str


class BookingCreate(BaseModel):
    customer: CustomerCreate
    total_price: float


class AirportResponse(BaseModel):
    airport_code: str
    name: str
    city: str
    state: str
    country: str


class FlightResponse(BaseModel):
    flight_number: str
    origin_airport: AirportResponse
    destination_airport: AirportResponse
    departure_time: str
    arrival_time: str
    status: str


class BaggageResponse(BaseModel):
    bag_id: str
    bag_type: str


class ReservationResponse(BaseModel):
    reservation_id: str
    flight: FlightResponse
    status: str
    fare_type: str
    boarding_position: str
    check_in_status: str
    bags: List[BaggageResponse]


class CustomerResponse(BaseModel):
    customer_id: str
    first_name: str
    last_name: str
    email: str
    phone_number: str


class BookingResponse(BaseModel):
    booking_id: str
    confirmation_number: str
    customer: CustomerResponse
    booking_date: str
    status: str
    total_price: float
    reservations: List[ReservationResponse]