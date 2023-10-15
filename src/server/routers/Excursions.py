from typing import List

from  fastapi import APIRouter

router = APIRouter()

from ..models import  Excursions


@router.get('/')
def get_excursions() -> List[Excursions]:
    return ({"ExcursionID": 1, "ExcursionName": "Poezdca", "price": 2434})


@router.get('/{ExcursionID}')
def get_currenr_excursions(ExcursionID: int) -> Excursions:
    return {"ExcursionID": ExcursionID, "ExcursionName": f"Экскурсия с id{ExcursionID}"}

@router.post('/')
def add_excursion(new_excursion: Excursions) -> Excursions:
    return {"id": 10, "ExcursionsName":new_excursion.ExcursionName}


@router.put('/{HotelID}')
def update_excursion(ExcursionID: int, updated_excursion: Excursions) -> Excursions:
    return {"ExcursionID": ExcursionID, "ExcursionName": updated_excursion.ExcursionName, "Price": updated_excursion.Price}


@router.delete("/{ExcursionID}")
def delete_hotels(ExcursionID: int) -> int:
    return 200

