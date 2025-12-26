from pydantic import BaseModel


class Stats(BaseModel):
    technologies: int
    projects: int
    collaborators: int