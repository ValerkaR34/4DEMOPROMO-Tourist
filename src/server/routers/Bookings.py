from typing import  List

from fastapi import APIRouter

router = APIRouter()

from ..models import  Bookings





@router.get('/')
def get_Bookings() -> List[Bookings]:
    return ({"BookingID": 1, "CustomerID": 2,"TourID": 3, "Booking_Date":"12.12.2094","PaymentStatus": "Не оплачен", "HotelID": 3})


@router.get('/{BookingID}')
def get_currenr_bookings(BookingID: int) -> Bookings:
    return {"BookingID": BookingID, "BookingName": f"бронированние  с id{BookingID}"}

@router.post('/')
def add_hotel(new_Bookings: Bookings) -> Bookings:
    return {"BookingID": 2, "PaymentStatus": new_Bookings.PaymentStatus, "BookingDate": new_Bookings.BookingDate}


@router.put('/{BookingID}')
def update_hotel(BookingID: int, updated_booking: Bookings) -> Bookings:
    return {"BookingID": BookingID, "Boking": updated_hotel.HotelName, "City": updated_hotel.City, "Country": updated_hotel.Country, "Rating": updated_hotel.Rating}


@router.delete("/{BookigsID}")
def delete_bookings(BookingsID: int) -> int:
    return 200