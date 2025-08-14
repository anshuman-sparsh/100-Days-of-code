from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Task 1
@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"} # http://127.0.0.1:8000


# Task 2
@app.get("/greet/{name}")
async def greet_user(name: str):
    return {"message": f"Hello, {name}!"} # http://127.0.0.1:8000/greet/Anshuman

# Task 3
@app.get("/square")
async def get_square(number: int):
    return {"result": number ** 2} # http://127.0.0.1:8000/square?number=5


# Task 4  # http://127.0.0.1:8000/docs  - Try it Out for POST /user for POST label.

# 1.
class User(BaseModel):
    name: str
    age: int

# 2.
@app.post("/user")
async def create_user(user: User):
    return {
        "status": "success",
        "user_received": {
            "name": user.name,
            "age": user.age
        }
    }