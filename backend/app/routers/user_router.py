
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.data.database import get_db
from app.schemas.token_schema import Token
from app.services.services_auth import AuthService


router = APIRouter(
    prefix="/users",
    tags=["user"]
)

@router.post(
    "/login",
    summary="Login a user"
)
def login_user(form_data: OAuth2PasswordRequestForm = Depends(), service: AuthService = Depends(AuthService)) -> Token:
    return service.authenticate_and_issue_token(email=form_data.username, password=form_data.password)


def get_service():
    return AuthService()