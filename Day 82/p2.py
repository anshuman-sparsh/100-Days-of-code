from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserWithDefaults(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    age: int | None = None

@app.post("/user_with_defaults")
async def create_user_with_defaults(user: UserWithDefaults):
    return user

# python -m uvicorn p2:app --reload
# http://127.0.0.1:8000/docs