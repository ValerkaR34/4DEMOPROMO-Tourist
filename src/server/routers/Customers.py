from typing import List

import fastapi

customer_router = fastapi.APIRouter(prefix="/customers", tags=["Customers"])

from ..models import Customers


from server.resolvers.customer import new_customer,update_customer,get_all_customer,get_customer,delete_customer

@customer_router.get("/")
def start_page():
    return ""

@customer_router.get('/get/')
def get_Customers() -> List[Customers]:
    return get_all_customer()


@customer_router.get('/{CustomerID}')
def get_currenr_Customers(CustomerID: int) -> Customers:
    return get_customer(CustomerID)

@customer_router.post('/')
def add_customers(customer: Customers) -> Customers:
    return new_customer(customer)


@customer_router.put('/update/{HotelID}')
def update_customers(CustomerID: int, updated_customer: Customers) -> Customers:
    return update_customer(Customers=updated_customer,CustomerID=CustomerID)

@customer_router.delete("/delete/{CustomerID}")
def delete_customers(CustomerID: int) -> int:
    return delete_customer(CustomerID)