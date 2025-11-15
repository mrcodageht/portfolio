from enum import Enum

from app.services.project_service import Project


class Kind(str, Enum):
    SCREENSHOT = "screenshot"
    LOGO = "logo"
    DIAGRAM = "diagram"
    THUMB = "thumb"

class ProjectImage:
    id: str
    project: Project
    imageUrl: str
    altText: str
    kind: Kind
