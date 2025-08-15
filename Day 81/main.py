from fastapi import FastAPI, Path, Query
from typing import Annotated

app = FastAPI()

# Task 1
@app.get("/items/{item_id}")
async def read_item(
    item_id: Annotated[int, Path(title="Item ID", gt=0)]
):  # Example: http://127.0.0.1:8000/items/5
    return {"item_id": item_id}


# Task 2
@app.get("/search")
async def search_items(
    q: Annotated[str, Query(title="Search query", min_length=3, max_length=50)]
):  # Example: http://127.0.0.1:8000/search?q=fastapi
    return {"results": f"You searched for: '{q}'"}


# Task 3
@app.get("/products")
async def read_products(
    limit: Annotated[int, Query(title="Limit", ge=1, le=100)] = 10
):  # Example: http://127.0.0.1:8000/products?limit=25
    return {"message": f"Displaying {limit} products."}


# Task 4 
@app.get("/users/{user_id}")
async def read_user(
    user_id: Annotated[int, Path(title="User ID", gt=0)],
    verbose: Annotated[bool, Query(title="Verbose output")] = False,
):  # Example: http://127.0.0.1:8000/users/123?verbose=true
    user_data = {"user_id": user_id, "name": f"User_{user_id}", "is_active": True}
    if verbose:
        user_data.update({"email": f"user{user_id}@example.com", "role": "member"})
    return user_data



# python -m uvicorn main:app --reload       = Run this in integrated terminal