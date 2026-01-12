
from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from fastapi.security import OAuth2PasswordRequestForm

from app.schemas.token_schema import KeyInit, Token
from app.services.services_auth import AuthService
from app.services.services_user import UserService
from app.schemas.user_schema  import UserChangePassword, UserResetPassword
from app.config.env import settings


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

@router.patch("/change-password")
def change_password(payload: UserChangePassword,service: UserService = Depends(UserService)):
    is_change = service.update_password(payload_change=payload)
    if is_change:
        return {"message":"Your password has been reset successfully"}
    return {"message":"Your password has not been reset successfully"}


    

@router.patch("/reset-password", status_code=status.HTTP_200_OK)
def reset_password(payload: UserResetPassword, service: UserService = Depends(UserService)):
    key = payload.key
    if key != settings.KEY_INIT:
        raise HTTPException(
            detail="The key is empty or invalid",
            status_code=status.HTTP_400_BAD_REQUEST
        )
    is_reset = service.update_password(payload_reset=payload)
    if is_reset:
        return {"message":"Your password has been reset successfully"}
    
    return {"message":"Your password has not been reset successfully"}

def get_service():
    return AuthService()