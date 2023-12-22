from ..models import  Tours

from server.db_manager.manager_db import base_manager

def new_tour(Tours: Tours):
    newt = base_manager.execute(f""" INSERT INTO TourGuides(TourName,StartDate,EndDate,Price)
                                VALUES (?,?,?,?) RETURNING TourID; """,
                                (Tours.TourName,Tours.Price,Tours.StartDate,Tours.EndDate))
    return newt


def get_tour(TourID: int):
    return base_manager.execute(query="SELECT TourID,TourName,StartDate,EndDate,Price FROM Tours WHERE TourID =?", args=(TourID,))

def get_all_tour():
    return base_manager.execute(query="SELECT TourID,TourName,StartDate,EndDate,Price FROM Tours", many=True)

def delete_tour(TourID:int):
    return base_manager.execute("DELETE From Tours WHERE TourID=?",
                                args=(TourID))

def update_tour(Tours: Tours, TourID: int):
    updaitc = base_manager.execute(f"""update Tours set (TourName,StartDate,EndDate,Price) = (?,?,?,?) where TourID=(?);""",
                                   (Tours.TourName,TourID,Tours.Price,Tours.StartDate,Tours.EndDate))

    return updaitc