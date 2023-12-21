from fastapi import FastAPI
import uvicorn

from fastapi.responses import RedirectResponse
from server.routers import hotels_router, Excursions_router, Bookings_router, Tours_router, Customers_router, tourguides_router, ExcursionBookings_router

app = FastAPI()


app.include_router(hotels_router, prefix="/hotels")
app.include_router(Bookings_router, prefix="/Bookings")
app.include_router(Excursions_router, prefix="/Excursions")
app.include_router(Tours_router, prefix="/Tours")
app.include_router(Customers_router, prefix="/Customers")
app.include_router(tourguides_router, prefix="/tourguides")
app.include_router(ExcursionBookings_router, prefix="/ExcursionBookings")

@app.get('/')
def root():
    return RedirectResponse('/docs')





if __name__ == '__main__':
    uvicorn.run(app="start_server:app", host="0.0.0.0", port=8000, reload=True)

# http://127.0.0.1:8000/ поэтому адресу запускается  ( а по http://0.0.0.0:8000/  нет )

 # uvicorn start_server:app --reload    - почему то через  "pyhton start_server.py" глючит, поэтому такой командой лучше

