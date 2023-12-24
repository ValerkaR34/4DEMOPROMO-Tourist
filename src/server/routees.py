from server.routers.hotels import hotels_router
from server.routers.Excursions import Excurs_router
from server.routers.Bookings import bookings_router
from server.routers.Customers import customer_router
from server.routers.tourguides import tourgGuides_router
from server.routers.Tours import Tours_router
from server.routers.ExcursionBookings import ExcursBook_router

routersval = (hotels_router,Excurs_router,bookings_router,customer_router,tourgGuides_router,Tours_router,ExcursBook_router)