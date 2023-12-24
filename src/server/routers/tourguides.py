from typing import List

import fastapi

tourgGuides_router = fastapi.APIRouter(prefix="/Guide", tags=["TourGuides"])

from server.sql_base.models  import TourGuides

from  server.resolvers.TourGuides import new_tourguidesy,get_guide,get_all_guide,delete_guide,update_guide

@tourgGuides_router.get("/")
def start_page():
    return ""

@tourgGuides_router.get('/')
def get_TourGuides() -> List[TourGuides]:
    return get_all_guide()

@tourgGuides_router.get('/{GuideID}')
def get_currenr_guide(GuideID: int) -> TourGuides:
    return get_guide(GuideID)

@tourgGuides_router.post('/')
def add_guide(new_tourguides: TourGuides) -> TourGuides:
    return new_tourguidesy(new_tourguides)


@tourgGuides_router.put('/{HotelID}')
def update_guidess(GuideID: int, updated_guides: TourGuides) -> TourGuides:
    return update_guide(TourGuides=updated_guides,GuideID=GuideID)

@tourgGuides_router.delete("/delete/{GuideID}")
def delete_guide(GuideID: int) -> int:
    return delete_guide(GuideID)