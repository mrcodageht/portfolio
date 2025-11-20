from typing import List

from fastapi import Depends

from ..data.dao.project_dao import ProjectDao
from ..models.project_model import ProjectModel
from app.schemas.project_schema import Project


class ProjectService:
    def __init__(self, project_dao: ProjectDao = Depends(ProjectDao)):
        self.project_dao = project_dao

    def get_all(self)-> list[type[ProjectModel]]:
        projects = self.project_dao.find_all()
        return projects

def get_project_dao():
    return ProjectDao

def map_to_project(project_model: ProjectModel) -> Project:
    return Project(
        pid=project_model.pid,
        title=project_model.title,
        slug=project_model.slug,
        description=project_model.description,
        startDate=project_model.start_at,
        endDate=project_model.end_at,
        status=project_model.status,
        visibility=project_model.visibility,
        coverImageUrl=project_model.cover_image_url,
        liveUrl=project_model.liveUrl,
        repoUrl=project_model.repoUrl,
    )