from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel
from typing import Optional

from app.schemas.collaborator_schema import CollaboratorPublic
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
    live_url: Optional[str] = None
    repo_url: Optional[str] = None

class ProjectTechnologyCreate(BaseModel):
    slug: str

class ProjectPublic(ProjectBase):
    pid: str

class ProjectPublicWithTechnologies(ProjectPublic):
    technologies: list[TechnologyPublic]

class ProjectPublicWithCollaborators(ProjectPublic):
    collaborators: list[CollaboratorPublic]

class ProjectPublicWithCollaboratorsAndTechnologies(ProjectPublic):
    technologies: list[TechnologyPublic]
    collaborators: list[CollaboratorPublic]
    

class ProjectUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    start_at: Optional[datetime] = None
    end_at : Optional[datetime] = None # souvent utile d'accepter None
    status: Optional[Status] = None
    visibility: Optional[Visibility] = None
    live_url: Optional[str] = None
    repo_url: Optional[str] = None

class ProjectExternal(BaseModel):
    name: Optional[str]
    description: Optional[str]
    created_at: Optional[str]
    status: str | None = str(Status.IN_PROGRESS)
    visibility: str | None = "published"

class ProjectGithub(ProjectExternal):
    svn_url: Optional[str]
    private: Optional[bool]
    
class ProjectGitlab(ProjectExternal):
   path: Optional[str]
   web_url: Optional[str] 


