"""Property request/response schemas."""
from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class PropertyCreate(BaseModel):
    """Property creation request schema."""
    title: str
    description: Optional[str] = None
    location: str
    price_per_night: float
    bedrooms: int
    bathrooms: int
    max_guests: int


class PropertyUpdate(BaseModel):
    """Property update request schema."""
    title: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    price_per_night: Optional[float] = None
    bedrooms: Optional[int] = None
    bathrooms: Optional[int] = None
    max_guests: Optional[int] = None


class PropertyResponse(BaseModel):
    """Property response schema."""
    id: int
    host_id: int
    title: str
    description: Optional[str]
    location: str
    price_per_night: float
    bedrooms: int
    bathrooms: int
    max_guests: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
