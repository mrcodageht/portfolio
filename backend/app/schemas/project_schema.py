from datetime import datetime

from pydantic import BaseModel
from enum import Enum

class Status(str, Enum):
    IN_PROGRESS = "in_progress"
    FINISHED = "finished"
    ARCHIVED = "archived"
    PLANNING = "planning"

class Visibility(str, Enum):
    PUBLISHED = "published"
    PRIVATE = "private"


class Portfolio(BaseModel):
    pid: str
    title: str
    slug: str
    description: str
    startDate: datetime
    endDate: datetime
    status: Status
    visibility: Visibility
    coverImageUrl: str
    liveUrl: str
    repoUrl: str


    def __eq__( self, other ):
        if not isinstance( other, Portfolio ):
            return NotImplemented
        return(
                self.pid == other.pid and
                self.title == other.title and
                self.slug == other.slug and
                self.description == other.description and
                self.startDate == other.startDate and
                self.endDate == other.endDate and
                self.status == other.Status and
                self.visibility == other.visibility and
                self.coverImageUrl == other.coverImageUrl and
                self.liveUrl == other.liveUrl and
                self.repoUrl == other.repoUrl 
        )