from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel
from enum import Enum
from typing import Any

class Status(str, Enum):
    IN_PROGRESS = "in_progress"
    FINISHED = "finished"
    ARCHIVED = "archived"
    PLANNING = "planning"

class Visibility(str, Enum):
    PUBLISHED = "published"
    PRIVATE = "private"

class Project(BaseModel):
    pid: str
    title: str
    slug: str
    description: str
    startDate: datetime
    endDate: datetime | None  # souvent utile d'accepter None
    status: Status
    visibility: Visibility
    coverImageUrl: str | None
    liveUrl: str | None
    repoUrl: str | None

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Project):
            return NotImplemented
        # Pydantic v1: .dict(); v2: .model_dump() — on essaie les deux pour compatibilité
        try:
            return self.model_dump() == other.model_dump()
        except Exception:
            return self.dict() == other.dict()
