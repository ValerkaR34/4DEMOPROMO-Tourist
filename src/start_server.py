from  fastapi import  FastAPI
import uvicorn


from  server.routees import routersval

from fastapi.responses import RedirectResponse


app = FastAPI(title="Tour-Valerii")

[app.include_router(routees) for routees in routersval]







@app.get('/')
def root():
    return RedirectResponse('/docs')





if __name__ == '__main__':
    uvicorn.run(app="start_server:app", host="0.0.0.0", port=8000, reload=True)

# http://127.0.0.1:8000/ поэтому адресу запускается  ( а по http://0.0.0.0:8000/  нет )

 # uvicorn start_server:app --reload    - почему то через  "pyhton start_server.py" глючит, поэтому такой командой лучше


# from server.sql_base.Rescript import base_manager
# from server.routees import routersval
# import fastapi
#
# base_manager.create_base('../sql/create_base.sql')
#
#
#
# app = fastapi.APIRouter()
#
# [app.include_router(routees) for routees in routersval]