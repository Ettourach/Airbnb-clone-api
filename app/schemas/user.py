"""User request/response schemas."""
from pydantic import BaseModel, EmailStr
from datetime import datetime
from enum import Enum


class UserRole(str, Enum):
    """User role enumeration."""
    GUEST = "guest"
    HOST = "host"


class UserRegister(BaseModel):
    """User registration request schema."""
    email: EmailStr
    username: str
    password: str
    full_name: str
    role: UserRole = UserRole.GUEST


class UserLogin(BaseModel):
    """User login request schema."""
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    """User response schema."""
    id: int
    email: str
    username: str
    full_name: str
    role: UserRole
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class TokenResponse(BaseModel):
    """Token response schema."""
    access_token: str
    token_type: str
