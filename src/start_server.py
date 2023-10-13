from fastapi import FastAPI
import uvicorn

from fastapi.responses import RedirectResponse
from src import router as group_hotels

app = FastAPI()


app.include_router(group_hotels, prefix="/hotels")

@app.get('/')
def root():
    return RedirectResponse('/docs')




if __name__ == '__main__':
    uvicorn.run(app="start_server:app", host="0.0.0.0", port=8000, reload=True)

# http://127.0.0.1:8000/ поэтому адресу запускается  ( а по http://0.0.0.0:8000/  нет )

 # uvicorn start_server:app --reload    - почему то через  "pyhton start_server.py" глючит, поэтому такой командой лучше

