"""Booking request/response schemas."""
from pydantic import BaseModel
from datetime import date, datetime
from enum import Enum
from typing import Optional


class BookingStatus(str, Enum):
    """Booking status enumeration."""
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"


class BookingCreate(BaseModel):
    """Booking creation request schema."""
    property_id: int
    check_in_date: date
    check_out_date: date


class BookingUpdate(BaseModel):
    """Booking update request schema."""
    status: Optional[BookingStatus] = None


class BookingResponse(BaseModel):
    """Booking response schema."""
    id: int
    guest_id: int
    property_id: int
    check_in_date: date
    check_out_date: date
    status: BookingStatus
    total_price: float
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
