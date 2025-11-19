from fastapi import APIRouter
from app.schemes.user_register import SUserRegister

router = APIRouter(
    prefix="/auth",
    tags=["auth & users"],
)


@router.get("/register")
def user_register(user_data: SUserRegister):
    pass
