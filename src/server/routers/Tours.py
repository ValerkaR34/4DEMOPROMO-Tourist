from typing import List

from  fastapi import APIRouter

router = APIRouter()

from ..models import  Tours


@router.get('/')
def get_tours() -> List[Tours]:
    return ({"TourID": 1, })


@router.get('/{ToursID}')
def get_currenr_tours(TourID: int) -> Tours:
    return {"TourID": TourID, "TourName": f"Тур с id{TourID}"}

@router.post('/')
def add_tours(new_tours: Tours) -> Tours:
    return {"id": 10, "TourName": new_tours.TourName}


@router.put('/{HotelID}')
def update_tours(TourID: int, updated_tours: Tours) -> Tours:
    return {"TourID": TourID, "TourName": updated_tours.TourName}


@router.delete("/{TourID}")
def delete_hotels(TourID: int) -> int:
    return 200