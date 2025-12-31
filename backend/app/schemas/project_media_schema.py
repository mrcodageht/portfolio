
from app.schemas.enums import Kind
from pydantic import BaseModel
from fastapi import File
from fastapi import Form


class ProjectMedia(BaseModel):
    alt_text: str
    kind: Kind

    @classmethod
    def as_form(
        cls,
        alt_text: str = Form(...),
        kind: Kind = Form(...)
    ):
        return cls(
            alt_text=alt_text,
            kind=kind
        )


class ProjectMediaCreate(ProjectMedia):
    media: str

class ProjectMediaPublic(ProjectMedia):
    id: str
    media_url: str
