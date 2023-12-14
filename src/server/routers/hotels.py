from typing import List

from  fastapi import APIRouter

router = APIRouter()

from ..models import  Hotels

from server.resolvers.hotel import  new_hotel,get_hotel,get_all_hotel,delete_hotel,update_hotel


@router.get('/')
def get_hotels() -> List[Hotels]:
    return get_all_hotel()


@router.get('/{HotelID}')
def get_currenr_hotel(HotelID: int) -> Hotels:
    return get_hotel(HotelID)

@router.post('/')
def add_hotel(new_hotel: Hotels) -> Hotels:
    return new_hotel(Hotels)


@router.put('/{HotelID}')
def updates_hotel(HotelID: int, updated_hotel: Hotels) -> Hotels:
    return update_hotel(Hotels=updated_hotel, HotelID=HotelID)


@router.delete("/{HotelID}")
def delete_hotels(HotelID: int) -> int:
    return delete_hotel(HotelID)