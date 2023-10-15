from typing import List

from fastapi import APIRouter

router = APIRouter()

from ..models import ExcursionBookings


@router.get('/')
def get_ExcursionBookingID() -> List[ExcursionBookings]:
    return ({"ExcursionBookingID": 3, "CustomerID": 3, "ExcursionID": 3, "BookingDate": "2023.11.08", "PaymentStatus": "Оплачено"})


@router.get('/{ExcursionBookingID}')
def get_currenr_ExcursionBooking(ExcursionBookingID: int) -> ExcursionBookings:
    return {"ExcursionBookingID": ExcursionBookingID, "": f"где бронирование с id{ExcursionBookingID}"}

@router.post('/')
def add_hotel(new_ExcursionBookings: ExcursionBookings) -> ExcursionBookings:
    return {"ExcursionBookingID": new_ExcursionBookings.ExcursionBookingID}


@router.put('/{ExcursionBookingID}')
def update_hotel(ExcursionBookingID: int, updated_ExcursionBookings: ExcursionBookings) -> ExcursionBookings:
    return {"ExcursionBookingsID": ExcursionBookingID, "BookingDate": updated_ExcursionBookings.BookingDate}


@router.delete("/{ExcursionBookingID}")
def delete_hotels(ExcursionBookingID: int) -> int:
    return 200