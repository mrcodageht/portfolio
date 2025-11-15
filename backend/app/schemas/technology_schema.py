from enum import Enum
from pydantic import BaseModel


class Type(str, Enum):
    BACKEND = "backend"
    FRONTEND = "frontend"
    DB = "db"
    DEVOPS = "devops"
    MOBILE = "mobile"
    TOOL = "tool"
    OTHER = "other"


class Technology(BaseModel):
    id: str
    name: str
    slug: str
    type: Type
    iconUrl: str