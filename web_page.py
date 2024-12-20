from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from database.dbGet import GetAll

router = APIRouter()
templates = Jinja2Templates(directory="templates")
get_all = GetAll()

@router.get("/webpage/home", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@router.get("/webpage/property", response_class=HTMLResponse)
async def properties(request: Request):
    properties = get_all.get_property()
    if not properties:
        raise HTTPException(status_code=404, detail="No properties found")
    return templates.TemplateResponse("property.html", {"request": request, "properties": properties})