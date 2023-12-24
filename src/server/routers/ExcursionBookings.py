from typing import List



import fastapi

ExcursBook_router = fastapi.APIRouter(prefix="/excursionBookings", tags=["ExcursionBookings"])

from server.resolvers.ExcursionBookings import new_Excurbook,delete_ExcursionBookings,update_ExcursionBookings,get_all_ExcursionBookings,get_ExcursionBookings

from server.sql_base.models import ExcursionBookings


@ExcursBook_router.get("/")
def start_page():
    return ""
@ExcursBook_router.get('/get/')
def get_ExcursionBookingID() -> List[ExcursionBookings]:
    return get_all_ExcursionBookings()


@ExcursBook_router.get('/get/{ExcursionBookingID}')
def get_currenr_ExcursionBooking(ExcursionBookingID: int) -> ExcursionBookings:
    return get_ExcursionBookings(ExcursionBookingID)

@ExcursBook_router.post('/new/')
def add_hotel(new_ExcursionBookings: ExcursionBookings) -> ExcursionBookings:
    return new_Excurbook(new_ExcursionBookings)


@ExcursBook_router.put('/update/{ExcursionBookingID}')
def update_hotel(ExcursionBookingID: int, updated_ExcursionBookings: ExcursionBookings) -> ExcursionBookings:
    return update_ExcursionBookings(ExcursionBookings=updated_ExcursionBookings, ExcursionBookingID=ExcursionBookingID)

@ExcursBook_router.delete("/delete/{ExcursionBookingID}")
def delete_hotels(ExcursionBookingID: int) -> int:
    return delete_ExcursionBookings(ExcursionBookingID)