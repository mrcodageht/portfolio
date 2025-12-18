from datetime import datetime
from pydantic import BaseModel

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

