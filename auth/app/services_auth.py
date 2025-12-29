import datetime

from fastapi import HTTPException
from jose import ExpiredSignatureError, jwt
from starlette import status
from app.config.env import settings
from app.token_schema import Token, TokenDecoded


def issue_token(email: str, admin: bool = False) -> Token:
    token = create_access_token(email=email, admin=admin)
    return Token(access_token=token)

def create_access_token(email: str, admin: bool = False) -> str:
    expire = datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"sub": email, "exp": expire, "admin": admin}
    return jwt.encode(to_encode, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)

def validate_token(token: str) -> TokenDecoded:
    try:
        decode_result = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
        token_decoded = TokenDecoded(**decode_result)

        if token_decoded.exp < datetime.datetime.now(datetime.timezone.utc):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Expired token")

        return token_decoded
    except ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Expired token")