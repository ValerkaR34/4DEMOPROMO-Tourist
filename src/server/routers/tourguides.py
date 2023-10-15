from typing import List

from  fastapi import APIRouter

router = APIRouter()

from ..models import TourGuides

@router.get('/')
def get_TourGuides() -> List[TourGuides]:
    return ({"GuideID:": 1, "First_name": "Anton", "Last_Name": "Volcov", "Email": "pugachev2004@yandex.ru"})

@router.get('/{GuideID}')
def get_currenr_guide(GuideID: int) -> TourGuides:
    return {"GuideID": GuideID, "First_Name": f"ГИД с id{GuideID}"}

@router.post('/')
def add_guide(new_tourguides: TourGuides) -> TourGuides:
    return {"id": 10, "HotelName": new_tourguides.FirstName}


@router.put('/{HotelID}')
def update_guide(GuideID: int, updated_guides: TourGuides) -> TourGuides:
    return {"GuideID": GuideID, "First_Name": updated_guides.FirstName, "Last_Name": updated_guides.LastName, "email": updated_guides.Email}


@router.delete("/{GuideID}")
def delete_guide(GuideID: int) -> int:
    return 200