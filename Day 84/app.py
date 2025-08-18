import sqlite3
import string
import random
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, HttpUrl

DATABASE = 'shortener.db'
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

class URLItem(BaseModel):
    url: HttpUrl

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def generate_short_code():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(6))

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/shorten")
async def create_short_url(url_item: URLItem, request: Request):
    original_url = str(url_item.url)
    db = get_db()
    
    # --- THIS IS THE UPDATED LOGIC ---
    
    # 1. Check if the URL already exists in the database.
    existing = db.execute(
        'SELECT short_code FROM urls WHERE original_url = ?', (original_url,)
    ).fetchone()
    
    if existing:
        short_code = existing['short_code']
    else:
        # 2. If it doesn't exist, generate a new, unique code.
        while True:
            short_code = generate_short_code()
            collision = db.execute(
                'SELECT id FROM urls WHERE short_code = ?', (short_code,)
            ).fetchone()
            if not collision:
                break # The code is unique
        
        # 3. Insert the new, unique mapping.
        db.execute('INSERT INTO urls (original_url, short_code) VALUES (?, ?)',
                   (original_url, short_code))
        db.commit()

    # --- END OF UPDATED LOGIC ---
    
    db.close()
    
    base_url = str(request.base_url)
    return {"short_url": f"{base_url}s/{short_code}"}

@app.get("/s/{short_code}")
async def redirect_url(short_code: str):
    db = get_db()
    url_data = db.execute(
        'SELECT original_url FROM urls WHERE short_code = ?', (short_code,)
    ).fetchone()
    db.close()
    
    if url_data:
        return RedirectResponse(url=url_data['original_url'])
    
    raise HTTPException(status_code=404, detail="URL not found")