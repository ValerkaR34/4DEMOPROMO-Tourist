from  ..sql_base.models import Bookings

from server.sql_base.Rescript import base_manager
def new_Bookngs(Bookings: Bookings):
    newq = base_manager.execute(f""" INSERT INTO Bookings(CustomerID,TourID,BookingDate,PaymentStatus,HotelID)
                                VALUES (?,?,?,?,?) RETURNING BookingID """,
                                (Bookings.BookingDate,Bookings.TourID,Bookings.HotelID,Bookings.PaymentStatus,Bookings.CustomerID))
    return newq

def get_booking(BookingsID: int):
    return base_manager.execute(query="SELECT BookingID,CustomerID,TourID,BookingDate,PaymentStatus,HotelID FROM Bookings WHERE BookingID=?", args=(BookingsID,))

def get_all_booking():
    return base_manager.execute(query="SELECT BookingID,CustomerID,TourID,BookingDate,PaymentStatus,HotelID FROM Bookings",many=True)


def delete_bookings(BookingID: int):
    return base_manager.execute("DELETE From Bookings WHERE BookingID=?",
                                args=(BookingID,))

def update_bookings(Bookings: Bookings, BookingID: int):
    updantic = base_manager.execute(f"""update Bookings set (CustomerID,TourID,BookingDate,PaymentStatus,HotelID FROM Bookings) = (?,?,?,?,?) where BookingID=(?);""",
                                    (Bookings.BookingDate,Bookings.TourID,Bookings.CustomerID,Bookings.PaymentStatus,BookingID,Bookings.HotelID))
    return updantic