from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from database.dbGet import GetAll, GetAdvanced

router = APIRouter()
templates = Jinja2Templates(directory="templates")
get_all = GetAll()
get_advanced = GetAdvanced()

@router.get("/webpage/home", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@router.get("/webpage/property", response_class=HTMLResponse)
async def properties(request: Request):
    properties = get_all.get_property()
    if not properties:
        raise HTTPException(status_code=404, detail="No properties found")
    return templates.TemplateResponse("property.html", {"request": request, "properties": properties})


@router.get("/webpage/client", response_class=HTMLResponse)
async def clients(request: Request):
    clients = get_all.get_client()
    users = get_advanced.get_lone_user()
    if not clients:
        raise HTTPException(status_code=404, detail="No clients found")
    return templates.TemplateResponse("client.html", {"request": request, "clients": clients, "users": users})

@router.get("/webpage/meeting", response_class=HTMLResponse)
async def meetings(request: Request):
    meetings = get_advanced.get_meetings_with_info()
    agents = get_all.get_agent()
    clients = get_all.get_client()
    properties = get_all.get_property()
    if not meetings:
        raise HTTPException(status_code=404, detail="No meetings found")
    if not agents:
        raise HTTPException(status_code=404, detail="No agents found")
    if not clients:
        raise HTTPException(status_code=404, detail="No clients found")
    if not properties:
        raise HTTPException(status_code=404, detail="No properties found")
    return templates.TemplateResponse("meeting.html", {"request": request, "meetings": meetings, "agents": agents, "clients": clients, "properties": properties})

@router.get("/webpage/sales", response_class=HTMLResponse)
async def sales(request: Request):
    sales = get_all.get_sales()
    if not sales:
        raise HTTPException(status_code=404, detail="No sales found")
    return templates.TemplateResponse("sales.html", {"request": request, "sales": sales})

@router.get("/webpage/repairs", response_class=HTMLResponse)
async def repairs(request: Request):
    repairs = get_advanced.get_repairs_with_property()
    properties = get_all.get_property()
    if not repairs:
        raise HTTPException(status_code=404, detail="No repairs found")
    if not properties:
        raise HTTPException(status_code=404, detail="No properties found")
    
    return templates.TemplateResponse("repairs.html", {"request": request, "repairs": repairs, "properties": properties})
