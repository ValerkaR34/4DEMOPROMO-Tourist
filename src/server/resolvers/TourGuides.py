from ..models import TourGuides
from server.db_manager.manager_db import base_manager

def new_tourguidesy(TourGuides: TourGuides):
    anew = base_manager.execute(f""" INSERT INTO TourGuides(FirstName,LastName,Email)
                                VALUES(?,?,?) RETURNING GuideID; """,
                                (TourGuides.FirstName,TourGuides.LastName,TourGuides.Email))
    return anew


def get_guide(GuideID: int):
    return base_manager.execute(query="SELECT GuideID,FirstName,LastName,Email FROM TourGuides WHERE GuideID=?",args=(GuideID,))

def get_all_guide():
    return base_manager.execute(query="SELECT GuideID,FirstName,LastName,Email FROM TourGuides", many=True)

def delete_guide(GuideID: int):
    return base_manager.execute(query='DELETE FROM TourGuides WHERE GuideID=?',
                                args=GuideID)

def update_guide(TourGuides: TourGuides, GuideID: int):
    update = base_manager.execute(f"""update TourGuides set (FirstName,LastName,Email) = (?,?,?) where GuideID=(?);""",
                                  (TourGuides.FirstName,TourGuides.LastName,TourGuides.Email,GuideID))
    return update