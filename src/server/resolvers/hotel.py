from  ..models import Hotels
from server.db_manager.manager_db import base_manager

def new_hotel(Hotels: Hotels):
    hot = base_manager.execute(f"""INSERT INTO Hotels(HotelName,City,Country,Rating)
                               VALUES(?,?,?,?) RETURNING HotelID; """,
                               (Hotels.HotelName,Hotels.City,Hotels.Country,Hotels.Rating))
    return hot

def get_hotel(HotelID: int):
    return base_manager.execute(query="SELECT HotelID,HotelName,City,Country,Rating FROM Hotels WHERE HotelID=?",args=(HotelID,))

def get_all_hotel():
    return base_manager.execute(query="SELECT HotelID,HotelName,City,Country,Rating FROM Hotels", many=True)

def delete_hotel(HotelsID: int):
    return base_manager.execute(query="DELETE FROM Hotels WHERE HotelID=?",
                                args=(HotelsID))

def update_hotel(Hotels: Hotels, HotelsID: int):
    update = base_manager.execute(f"""update Hotels set (HotelName,City,Country,Rating) = (?,?,?,?) where HotelsID=(?);""",
                                  (Hotels.HotelName,Hotels.City,Hotels.Country,Hotels.Rating,HotelsID))
    return update