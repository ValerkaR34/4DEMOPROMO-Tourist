from ..models import ExcursionBookings

from ..db_manager.manager_db import base_manager

def new_Excurbook(ExcursionBookings: ExcursionBookings):
    vat = base_manager.execute(f""" INSERT INTO ExcursionBookings(CustomerID,ExcursionID,BookingDate,PaymentStatus)
                               VALUES(?,?,?,?) RETURNING ExcursionBookingID;""",
                               (ExcursionBookings.BookingDate,ExcursionBookings.ExcursionID,ExcursionBookings.CustomerID,ExcursionBookings.PaymentStatus))

    return vat

def get_ExcursionBookings(ExcursionBookingID: int):
    return base_manager.execute(query="SELECT ExcursionBookingID,ExcursionID,CustomerID,BokingDate,PaymentStatus FROM ExcursionBookings WHERE ExcursionBookingID=?",
                                args=(ExcursionBookingID,))

def get_all_ExcursionBookings():
    return base_manager.execute(query="SELECT ExcursionBookingID,ExcursionID,CustomerID,BokingDate,PaymentStatus FROM ExcursionBookings", many=True)

def delete_ExcursionBookings(ExcursionBookingID: int):

    return base_manager.execute(query="DELETE FROM ExcursionBookings WHERE ExcursionBookingID=?",
                                args=(ExcursionBookingID))

def update_ExcursionBookings(ExcursionBookings: ExcursionBookings, ExcursionBookingID: int):
    update = base_manager.execute(f"""update ExcursionBookings set (ExcursionID,CustomerID,BokingDate,PaymentStatus) = (?,?,?,?) where  ExcursionBookingID=(?);""",
                                  (ExcursionBookings.BookingDate,ExcursionBookings.ExcursionID,ExcursionBookings.CustomerID,ExcursionBookings.PaymentStatus,ExcursionBookingID))

    return update