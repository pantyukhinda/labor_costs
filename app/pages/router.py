from pathlib import Path

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/pages", tags=["Фронтенд"])

# Resolve templates from app package
_templates_dir = Path(__file__).resolve().parent.parent / "templates"
templates = Jinja2Templates(directory=str(_templates_dir))


@router.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.get("/login")
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@router.get("/register")
async def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@router.get("/organizations")
@router.get("/Organizations")
async def organizations_page(request: Request):
    return templates.TemplateResponse("organizations.html", {"request": request})


@router.get("/projects")
async def projects_page(request: Request):
    return templates.TemplateResponse("projects.html", {"request": request})


@router.get("/divisions")
async def divisions_page(request: Request):
    return templates.TemplateResponse("divisions.html", {"request": request})


@router.get("/activity-types")
async def activity_types_page(request: Request):
    return templates.TemplateResponse("activity_types.html", {"request": request})


@router.get("/tasks")
async def tasks_page(request: Request):
    return templates.TemplateResponse("tasks.html", {"request": request})


@router.get("/logout")
async def logout_page(request: Request):
    return templates.TemplateResponse("logout.html", {"request": request})
