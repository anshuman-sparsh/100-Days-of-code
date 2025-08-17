import sqlite3
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# --- Configuration ---
DATABASE = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'blog.db')
app = FastAPI()

# --- Pydantic Model ---
class Post(BaseModel):
    id: int
    title: str
    content: str
    created_at: str

# --- Database Functions (reused from Day 75) ---
def get_db():
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db

def get_post(post_id: int):
    db = get_db()
    post = db.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
    db.close()
    return post

# --- FastAPI API Endpoints ---
@app.get("/")
async def read_root():
    return {"message": "Welcome to the Blog API. Visit /api/posts to see all posts."}

# Task 1.1: Return all posts
@app.get("/api/posts", response_model=List[Post])
async def get_all_posts():
    db = get_db()
    posts_from_db = db.execute('SELECT * FROM posts ORDER BY created_at DESC').fetchall()
    db.close()
    return [dict(row) for row in posts_from_db]

# Task 1.2: Return a specific post
@app.get("/api/posts/{post_id}", response_model=Post)
async def get_single_post(post_id: int):
    post = get_post(post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return dict(post)

# Task 1.3: Return the last 3 posts
@app.get("/api/recent", response_model=List[Post])
async def get_recent_posts():
    db = get_db()
    posts_from_db = db.execute('SELECT * FROM posts ORDER BY created_at DESC LIMIT 3').fetchall()
    db.close()
    return [dict(row) for row in posts_from_db]

# Run: python -m uvicorn app:app --reload

# All Posts: http://127.0.0.1:8000/api/posts

# Single Post: http://127.0.0.1:8000/api/posts/1

# Recent Posts: http://127.0.0.1:8000/api/recent

# Interactive Docs: http://127.0.0.1:8000/docs