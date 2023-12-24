from typing import List

import fastapi

Excurs_router = fastapi.APIRouter(prefix="/excursions",tags=["Excursions"])

import fastapi

from  server.sql_base.models  import  Excursions

from server.resolvers.Excursions import get_excur,get_all_excur,delete_excur,update_excur,new_excurs

@Excurs_router.get("/")
def start_page():
    return ""

@Excurs_router.get('/get/')
def get_excursions() -> List[Excursions]:
    return get_all_excur()


@Excurs_router.get('/get/{ExcursionID}')
def get_currenr_excursions(ExcursionID: int) -> Excursions:
    return get_excur(ExcursionID)

@Excurs_router.post('/new/')
def add_excursion(new_excursion: Excursions) -> Excursions:
    return new_excurs(new_excursion)


@Excurs_router.put('/update/{HotelID}')
def update_excursion(ExcursionID: int, updated_excursion: Excursions) -> Excursions:
    return update_excur(Excursions=updated_excursion, ExcursionID=ExcursionID)


@Excurs_router.delete("/delete/{ExcursionID}")
def delete_excursion(ExcursionID: int) -> int:
    return delete_excur(ExcursionID)

