
from fastapi import Depends, HTTPException

from app.exceptions.global_projects_exceptions import ProjectAlreadyExistsWithSlugException,  ProjectNotFoundWithPidException

from ..data.dao.project_dao import ProjectDao
from ..models.project_model import ProjectModel
from app.schemas.enums import Status, Visibility
from app.schemas.project_schema import ProjectPublic, ProjectBase, ProjectUpdate
from starlette import status as s


class ProjectService:
    def __init__(self, project_dao: ProjectDao = Depends(ProjectDao)):
        self.project_dao = project_dao

    def get_all(
            self,
            status : Status | None = None,
            visibility : Visibility | None = None
    )-> list[ProjectPublic]:
        projects = self.project_dao.find_all( status=status, visibility=visibility)
        return [map_to_project(p) for p in projects]

    def get_by_pid(self, pid: str) -> ProjectPublic:
        project = self.project_dao.find_by_id(pid=pid)
        if project is None:
            raise ProjectNotFoundWithPidException(pid)
        return map_to_project(project_model=project)

    def save(self, project_create : ProjectBase) -> ProjectPublic:
        if project_create.slug is None:
            slug = project_create.title.replace(" ","-")
            project_create.slug = slug
            
        project_with_slug = self.project_dao.find_by_slug(project_create.slug)
        
        if project_with_slug is not None:
            # Si nous trouvons un objet, c'est que le slug existe déjà.
            print(f"project with slug : {project_with_slug}")
            raise ProjectAlreadyExistsWithSlugException(project_with_slug.slug)
        else:
            # Si project_with_slug est None, le slug est libre.
            print("==> block else")
            project_created = self.project_dao.create(project_create)
            return map_to_project(project_model=project_created)

    def update(self,pid, proj_to_update: ProjectUpdate) -> ProjectModel:
        proj_updated = self.project_dao.update(id=pid, item=proj_to_update)
        return map_to_project(proj_updated)

    def delete(self, pid: str):
        self.project_dao.delete(id=pid) 




def get_project_dao():
    return ProjectDao

def map_to_project(project_model: type[ProjectModel]) -> ProjectPublic:
    return ProjectPublic(
        title=project_model.title,
        pid=str(project_model.pid),
        slug=project_model.slug,
        description=project_model.description,
        start_at=project_model.start_at,
        end_at=project_model.end_at,
        status=project_model.status,
        visibility=project_model.visibility,
        cover_image_url=project_model.cover_image_url,
        live_url=project_model.live_url,
        repo_url=project_model.repo_url,
    )