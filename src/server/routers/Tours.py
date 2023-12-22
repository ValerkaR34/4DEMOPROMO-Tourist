from typing import List

import fastapi

Tours_router = fastapi.APIRouter(prefix="/tours", tags=["Tours"])

from ..models import  Tours

from server.resolvers.Tours import new_tour,get_tour,get_all_tour,delete_tour,update_tour

@Tours_router.get("/")
def start_page():
    return ""
@Tours_router.get('/get/')
def get_tours() -> List[Tours]:
    return get_all_tour()


@Tours_router.get('/get/{ToursID}')
def get_currenr_tours(TourID: int) -> Tours:
    return get_tour(TourID)

@Tours_router.post('/new/')
def add_tours(Tours: Tours) -> Tours:
    return new_tour(Tours)


@Tours_router.put('/update/{HotelID}')
def updates_tours(TourID: int, updated_tours: Tours) -> Tours:
    return update_tour(Tours=updated_tours, TourID=TourID)


@Tours_router.delete("/delete/{TourID}")
def delete_tours(TourID: int) -> int:
    return delete_tour(TourID)