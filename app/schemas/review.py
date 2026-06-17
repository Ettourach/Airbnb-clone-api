"""Review request/response schemas."""
from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class ReviewCreate(BaseModel):
    """Review creation request schema."""
    booking_id: int
    rating: int
    comment: Optional[str] = None


class ReviewResponse(BaseModel):
    """Review response schema."""
    id: int
    booking_id: int
    property_id: int
    guest_id: int
    rating: int
    comment: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
