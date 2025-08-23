from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# FastAPI is an ASGI application, built for high performance and async capabilities.
app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    # This route just shows the initial form
    return templates.TemplateResponse("index.html", {"request": request, "result": ""})

@app.post("/analyze", response_class=HTMLResponse)
async def analyze_number(request: Request, number: int = Form(...)):
    # FastAPI uses `Form(...)` to get form data and automatically validates the type
    
    # The core logic
    if number % 2 == 0:
        result = f"The number {number} is Even."
    else:
        result = f"The number {number} is Odd."
        
    # Render the same template, passing the result back
    return templates.TemplateResponse("index.html", {"request": request, "result": result})

# Run -> cd "Day 89/fastapi_app"
# then run -> python -m uvicorn main:app --reload