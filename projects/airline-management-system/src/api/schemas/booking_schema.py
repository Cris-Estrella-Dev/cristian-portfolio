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
