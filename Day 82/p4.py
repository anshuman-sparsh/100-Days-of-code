from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Book(BaseModel):
    title: str
    author: str

@app.get("/book", response_model=Book)
async def get_book():
    book_data_from_db = {
        "title": "1984",
        "author": "George Orwell",
        "year": 1949
    }
    return book_data_from_db

# python -m uvicorn p4:app --reload
# Endpoint URL: http://127.0.0.1:8000/book
# Interactive docs: http://127.0.0.1:8000/docs