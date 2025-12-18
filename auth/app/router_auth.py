from fastapi import APIRouter, Depends, Form
from starlette import status

from app.services_auth import issue_token, validate_token
from app.token_schema import TokenDecoded


router = APIRouter()

@router.post("/token")
def authenticate(email: str = Form(...), admin: bool = Form(False)):
    return issue_token(email, admin)

@router.post("/token/validate")
def validate(token: str = Form(...)) -> TokenDecoded:
    return validate_token(token)
