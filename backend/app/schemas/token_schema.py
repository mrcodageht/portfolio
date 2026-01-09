from datetime import datetime
from pydantic import BaseModel


# Représente un token d'accès pour l'affichage à l'utilisateur
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenDecoded(BaseModel):
    sub: str
    exp: datetime
    admin: bool = False


class KeyInit(BaseModel):
    key: str
