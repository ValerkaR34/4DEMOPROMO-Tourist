from typing import List

import fastapi

hotels_router = fastapi.APIRouter(prefix="/hotels", tags=["Hotels"])

from server.sql_base.models import Hotels

from server.resolvers.hotel import new_hotel,get_hotel,get_all_hotel,delete_hotel,update_hotel

@hotels_router.get("/")
def start_page():
    return ""

@hotels_router.get('/get/')
def get_hotels() -> List[Hotels]:
    return get_all_hotel()


@hotels_router.get('/get/{HotelID}')
def get_currenr_hotel(HotelID: int) -> Hotels:
    return get_hotel(HotelID)

@hotels_router.post('/new/')
def add_hotel(hotel: Hotels) -> Hotels:
    return new_hotel(hotel)


@hotels_router.put('/update/{HotelID}')
def updates_hotel(HotelID: int, updated_hotel: Hotels) -> Hotels:
    return update_hotel(Hotels=updated_hotel, HotelID=HotelID)


@hotels_router.delete("/delete/{HotelID}")
def delete_hotels(HotelID: int) -> int:
    return delete_hotel(HotelID)