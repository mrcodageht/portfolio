from pydantic import BaseModel

from app.schemas.enums import Type


class Technology(BaseModel):
    id: str
    name: str
    slug: str
    type: Type
    icon_url: str

class TechnologyCreate(BaseModel):
    name: str
    type: Type
    icon_url: str

class TechnologyPublic(TechnologyCreate):
    id: str
    slug: str

