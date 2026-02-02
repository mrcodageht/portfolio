from fastapi import HTTPException
from fastapi.params import Depends
from app.data.dao.user_dao import UserDao
from app.schemas.token_schema import Token, TokenDecoded
import bcrypt
import requests
from starlette import status
from sqlalchemy.orm import Session

from app.config.env import settings


class AuthService:
    def __init__(self, dao: UserDao = Depends(UserDao)):
        self.dao = dao

    def authenticate_and_issue_token(self, email: str, password: str) -> Token:
        user = self.dao.get_user_by_email(email=email)
        if not user or not verify_password(password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect credentials.",
                headers={"WWW-Authenticate": "Bearer"},
            )

        try:
            response = requests.post(
                settings.AUTH_TOKEN_ENDPOINT,
                {
                    "username": user.email,
                    "admin": user.admin,
                }
            )
        except Exception:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

        if response.status_code != status.HTTP_200_OK:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to obtain token from auth service",
            )

        token_data = response.json()
        return Token(**token_data)

def validate_token(token: str) -> TokenDecoded:
    try:
        response = requests.post(
            settings.AUTH_TOKEN_VALIDATE_ENDPOINT,
            {
                "token": token
            }
        )
    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    if response.status_code == status.HTTP_403_FORBIDDEN:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=response.json()["detail"])
    
    if response.status_code == status.HTTP_401_UNAUTHORIZED:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=response.json()["detail"])

    if response.status_code != status.HTTP_200_OK:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to validate token from auth service",
        )

    token_data = response.json()
    return TokenDecoded(**token_data)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))


def get_password_hash(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

def get_dao():
    return UserDao()