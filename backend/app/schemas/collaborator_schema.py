

from typing import Optional
from pydantic import BaseModel

class CollaboratorCreate(BaseModel):
    first_name: str
    last_name: str
    role: str
    portfolio_url: Optional[str] = None
    github_url: Optional[str] = None
    #gitlab_url: Optional[str] = None
    linkedin_url: Optional[str] = None

class CollaboratorPublic(CollaboratorCreate):
    id: str
        
