from typing import List

from  fastapi import  APIRouter

router = APIRouter

from ...models import  Hotels


@router.get('/')
def get_hotels() -> List[Hotels]:
    return ({"HotelID": 1, "HotelName": "Rar", "City":"Jason","Country": "Russia", "Rating": "4.4"})


@router.get('/{HotelID}')
def get_currenr_hotel(HotelID: int) -> Hotels:
    return {"HotelID": HotelID, "HotelName": f"Отель с id{HotelID}"}

@router.post('/')
def add_Hotel(new_hotel: Hotels) -> Hotels:
    return {"id": 10, "HotelName": new_hotel.HotelName}


@router.put('/{HotelID}')
def update_hotel(HotelID: int, updated_hotel: Hotels) -> Hotels:
    return {"HotelID": HotelID, "HotelName": updated_hotel.name, "City": updated_hotel.city, "Country": updated_hotel.country, "Rating": updated_hotel.rating}


@router.delete("/{HotelID}")
def delete_hotels(HotelID: int) -> int:
    return 200