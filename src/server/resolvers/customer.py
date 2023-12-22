from ..models import Customers

from server.db_manager.manager_db import base_manager

def new_customer(Customerss: Customers):
    newc = base_manager.execute(f"""INSERT INTO Customers(FirstName,LastName,Email) VALUES(?,?,?) RETURNING CustomerID; """,
                                (Customerss.FirstName,Customerss.LastName,Customerss.Email))
    return newc

def update_customer(Customeers: Customers, CustomerID: int):
    upd = base_manager.execute(f"""update Customers set (FirstName,LastName,Email) = (?,?,?) where CustomerID=(?);""",
                               (Customeers.FirstName,Customeers.LastName,CustomerID,Customeers.Email))
    return upd


def delete_customer(CustomerID: int):
    return base_manager.execute(query="DELETE FROM Customers WHERE CustomerID=?",
                                args=(CustomerID))
    

def get_customer(CustomerID: int):
    return base_manager.execute(query="SELECT CustomerID, FirstName,LastName,Email FROM Customers WHERE CustomerID=?", args=(CustomerID,))

def get_all_customer():
    return base_manager.execute(query="SELECT CustomerID,FirstName,LastName,Email FROM Customers", many=True)