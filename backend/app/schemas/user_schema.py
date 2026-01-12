from datetime import datetime
from pydantic import BaseModel
from app.schemas.token_schema import KeyInit

class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    admin: bool


class UserPublic(UserBase):
    id: str
    created_at: datetime
                 
class UserCreation(UserBase):
    hashed_password: str

class UserChangePassword(BaseModel):
    old_password: str
    new_password: str

class UserResetPassword(KeyInit):
    new_password: str