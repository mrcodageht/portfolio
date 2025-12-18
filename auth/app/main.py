from typing import Annotated
from app.services_auth import issue_token, validate_token
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends, Form, HTTPException
from fastapi import FastAPI
from datetime import timedelta
from starlette import status

from app.auth_utils import *
from app.models import *
from app.token_schema import TokenDecoded


app = FastAPI()



@app.post("/token")
def authenticate(username: str = Form(...), admin: bool = Form(False)):
    return issue_token(username, admin)

@app.post("/token/validate")
def validate(token: str = Form(...)) -> TokenDecoded:
    return validate_token(token)

