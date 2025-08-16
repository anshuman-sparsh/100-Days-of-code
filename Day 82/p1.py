from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str

@app.post("/user")
async def create_user(user: User):
    return user

# python -m uvicorn p1:app --reload
# http://127.0.0.1:8000/docs