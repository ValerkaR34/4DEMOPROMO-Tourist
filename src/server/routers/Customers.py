from typing import List

from fastapi import APIRouter

router = APIRouter()

from ..models import Customers


@router.get('/')
def get_Customers() -> List[Customers]:
    return ({"CustomerID": 1, "First_name": "Rysi", "Last_Name": "Vilca", "Email": "puvarachev2034@yandex.ru"})


@router.get('/{CustomerID}')
def get_currenr_Customers(CustomerID: int) -> Customers:
    return {"CustomerID": CustomerID}

@router.post('/')
def add_customers(new_customers: Customers) -> Customers:
    return {"id": 12, "Fitst_Name": new_customers.FirstName}


@router.put('/{HotelID}')
def update_customers(CustomerID: int, updated_customer: Customers) -> Customers:
    return {"CustomerID": CustomerID, "First_Name": updated_customer.FirstName, "email": updated_customer.Email}


@router.delete("/{CustomerID}")
def delete_customers(CustomerID: int) -> int:
    return 200