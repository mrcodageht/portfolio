from pydantic import BaseModel

from app.schemas.enums import Type


class Technology(BaseModel):
    id: str
    name: str
    slug: str
    type: Type
    iconUrl: str