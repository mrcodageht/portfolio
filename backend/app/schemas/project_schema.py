from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel
from typing import Any, Optional

from app.models.project_model import ProjectModel
from app.schemas.enums import Status, Visibility
from app.schemas.technology_schema import TechnologyPublic


class ProjectBase(BaseModel):
    title: str
    slug: Optional[str] = None
    description: str
    start_at: datetime
    end_at: Optional[datetime] = None  # souvent utile d'accepter None
    status: Status
    visibility: Visibility
    cover_image_url: Optional[str] = None
    live_url: Optional[str] = None
    repo_url: Optional[str] = None

def map_from_project_model(pm: type[ProjectModel]):
    return ProjectPublic(
        pid=str(pm.pid),
        title=pm.title,
        slug=pm.slug,
        description=pm.description,
        start_at=pm.start_at,
        end_at=pm.end_at,
        status=pm.status,
        visibility=pm.visibility,
        cover_image_url=pm.cover_image_url,
        live_url=pm.live_url,
        repo_url=pm.repo_url
    )


class ProjectPublic(ProjectBase):
    pid: str

class ProjectPublicWithTechnologies(BaseModel):
    project: ProjectPublic
    technologies: list[TechnologyPublic]

class ProjectUpdate(ProjectBase):
    title: Optional[str] = None
    description: Optional[str] = None
    start_at: Optional[datetime] = None
    end_at : Optional[datetime] = None # souvent utile d'accepter None
    status: Optional[Status] = None
    visibility: Optional[Visibility] = None
    cover_image_url: Optional[str] = None
    live_url: Optional[str] = None
    repo_url: Optional[str] = None
