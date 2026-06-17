"""Custom exception classes."""
from fastapi import HTTPException, status


class UserNotFoundError(HTTPException):
    """Exception raised when a user is not found."""
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )


class PropertyNotFoundError(HTTPException):
    """Exception raised when a property is not found."""
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Property not found",
        )


class BookingNotFoundError(HTTPException):
    """Exception raised when a booking is not found."""
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Booking not found",
        )


class EmailAlreadyExistsError(HTTPException):
    """Exception raised when email is already registered."""
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )


class InvalidCredentialsError(HTTPException):
    """Exception raised when credentials are invalid."""
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )


class PermissionDeniedError(HTTPException):
    """Exception raised when user lacks required permissions."""
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Permission denied",
        )


class OverlappingBookingError(HTTPException):
    """Exception raised when booking dates overlap."""
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Property is already booked for these dates",
        )
