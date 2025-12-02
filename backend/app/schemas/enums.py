from enum import Enum


class Status(str, Enum):
    IN_PROGRESS = "in_progress"
    FINISHED = "finished"
    ARCHIVED = "archived"
    PLANNING = "planning"

class Visibility(str, Enum):
    PUBLISHED = "published"
    PRIVATE = "private"
class Kind(str, Enum):
    SCREENSHOT = "screenshot"
    LOGO = "logo"
    DIAGRAM = "diagram"
    THUMB = "thumb"

class Type(str, Enum):
    BACKEND = "backend"
    FRONTEND = "frontend"
    DB = "db"
    DEVOPS = "devops"
    MOBILE = "mobile"
    TOOL = "tool"
    OTHER = "other"
