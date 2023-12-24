from typing import List

import fastapi

bookings_router = fastapi.APIRouter(prefix="/bookings", tags=["Bookings"])

from server.sql_base.models  import  Bookings

from server.resolvers.Bookings import new_Bookngs,update_bookings,delete_bookings,get_booking,get_all_booking



@bookings_router.get("/")
def start_page():
    return ""

@bookings_router.get('/get/')
def get_Bookings():
    return get_all_booking()

@bookings_router.get('/get/{BookingID}')
def get_currenr_bookings(BookingID: int) -> Bookings:
    return get_booking(BookingID)

@bookings_router.post('/new/')
def add_hotel(ne_Bookings: Bookings) -> Bookings:
    return new_Bookngs(ne_Bookings)


@bookings_router.put('/update/{BookingID}')
def update_hotel(BookingID: int, updated_booking: Bookings) -> Bookings:
    return update_bookings(Bookings=updated_booking,BookingID=BookingID)


@bookings_router.delete("/delete/{BookigsID}")
def delete_bookings(BookingsID: int) -> int:
    return delete_bookings(BookingsID)