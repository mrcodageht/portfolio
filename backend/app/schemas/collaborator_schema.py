

from typing import Optional
from pydantic import BaseModel

class CollaboratorCreate(BaseModel):
    firstname: str
    lastname: str
    role: str
    portfolioUrl: Optional[str] = None
    githubUrl: Optional[str] = None
    gitlabUrl: Optional[str] = None
    linkedinUrl: Optional[str] = None

class CollaboratorPublic(CollaboratorCreate):
    id: str
        
