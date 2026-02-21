from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates

from organizations.router import get_all_organizations

router = APIRouter(prefix="/pages", tags=["Фронтенд"])

templates = Jinja2Templates(directory="/templates")


@router.get("/Organizations")
async def get_organizations_page(
    request: Request,
    organizations=Depends(get_all_organizations),
):
    return templates.TemplateResponse(
        name="organizations.html",
        context={"request": request, "organizations": organizations},
    )
