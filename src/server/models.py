from pydantic import BaseModel
from datetime import date
from typing import Optional



class Customers(BaseModel):
    CustomerID: int
    FirstName: str
    LastName: str
    Email: str



class Tours(BaseModel):
    TourID: int
    TourName: str
    StartDate: date
    EndDate: date
    Price: int



class Hotels(BaseModel):
    HotelID: int
    HotelName: str
    City: str
    Country: str
    Rating: Optional[float]



class Bookings(BaseModel):
    BookingID: int
    CustomerID: int
    TourID: int
    BookingDate: date
    PaymentStatus: str
    HotelID: int


class Payments(BaseModel):
    PaymentID: int
    BookingID: int
    PaymentAmount: int


class TourGuides(BaseModel):
    GuideID: int
    FirstName: str
    LastName: str
    Email: str


class TouristGroups(BaseModel):
    GroupID: int
    TourID: int
    GuideID: int
    DepartureDate: date


class TouristGroupMembers(BaseModel):
    MemberID: int
    GroupID: int
    CustomerID: int


class Excursions(BaseModel):
    ExcursionID: int
    ExcursionName: str
    Price: int


class ExcursionBookings(BaseModel):
    ExcursionBookingID: int
    CustomerID: int
    ExcursionID: int
    BookingDate: date
    PaymentStatus: str


