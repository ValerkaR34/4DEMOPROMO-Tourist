from fastapi import FastAPI

app = FastAPI(
  title="Tour-app" )


test = [{"id": 1, "role": "admin"}, ]

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return [user for user in test if user.get("id") == user_id]