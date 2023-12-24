from  ..sql_base.models import Hotels

from server.sql_base.Rescript import base_manager

def new_hotel(Hotels: Hotels):
    hot = base_manager.execute(f"""INSERT INTO Hotels(HotelName,City,Country,Rating)
                               VALUES(?,?,?,?) RETURNING HotelID; """,
                               (Hotels.HotelName,Hotels.City,Hotels.Country,Hotels.Rating))
    return hot

def get_hotel(HotelID: int):
    return base_manager.execute(query="SELECT HotelID,HotelName,City,Country,Rating FROM Hotels WHERE HotelID=?",args=(HotelID,))

def get_all_hotel():
    return base_manager.execute(query="SELECT HotelID,HotelName,City,Country,Rating FROM Hotels", many=True)

def delete_hotel(HotelID: int):
    return base_manager.execute(query="DELETE FROM Hotels WHERE HotelID=?",
                                args=(HotelID,))

def update_hotel(Hotels: Hotels, HotelID: int):
    update = base_manager.execute(f"""update Hotels set (HotelName,City,Country,Rating) = (?,?,?,?) where HotelID=(?);""",
                                  (Hotels.HotelName,Hotels.City,Hotels.Country,Hotels.Rating,HotelID))
    return update