from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 💡 You must include the User model here for the Post model to use it.
class User(BaseModel):
    id: int
    name: str
    email: str

class Post(BaseModel):
    title: str
    content: str
    author: User  # Nested Pydantic model

@app.post("/post")
async def create_post(post: Post):
    return post

# python -m uvicorn p3:app --reload
# http://127.0.0.1:8000/docs