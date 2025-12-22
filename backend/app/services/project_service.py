
from fastapi import Depends, HTTPException

from app.data.dao.collaborator_dao import CollaboratorDao
from app.data.dao.technology_dao import TechnologyDao
from app.exceptions.global_projects_exceptions import ProjectAlreadyExistsWithSlugException,  ProjectNotFoundWithPidException
from app.utils.mapping_utils import map_to_project, map_to_project_with_collaborators, map_to_project_with_technologies, map_to_project_with_technologies_and_collaborators

from ..data.dao.project_dao import ProjectDao
from ..models.project_model import ProjectModel, TechnologyModel
from app.schemas.enums import Status, Visibility
from app.schemas.project_schema import ProjectPublic, ProjectBase, ProjectPublicWithTechnologies, ProjectUpdate
from starlette import status as s


class ProjectService:
    def __init__(
            self, 
            project_dao: ProjectDao = Depends(ProjectDao),
            technology_dao: TechnologyDao = Depends(TechnologyDao),
            collaborator_dao: CollaboratorDao = Depends(CollaboratorDao)
            ):
        self.project_dao = project_dao
        self.technology_dao = technology_dao
        self.collaborator_dao = collaborator_dao

    def get_all(
            self,
            status : Status | None = None,
            visibility : Visibility | None = None,
            techs: bool = False,
            collabs: bool = False
    )-> list[ProjectPublic] | list[ProjectPublicWithTechnologies]:
            
        projects = self.project_dao.find_all( status=status, visibility=visibility)
        if techs and collabs:
            project_with_collabs_and_techs = []
            for p in projects:
                collabs = self.collaborator_dao.find_by_project(project_id=p.pid)
                technos = self.technology_dao.find_by_project(project_id=p.pid)
                project_with_collabs_and_techs.append(map_to_project_with_technologies_and_collaborators(
                    project_model=p,
                    collabs=collabs,
                    techs=technos
                ))
            return project_with_collabs_and_techs

        if techs:
            print("Requested technologies")
            project_with_techs = []
            for p in projects:
                technos = self.technology_dao.find_by_project(project_id=p.pid)
                project_with_techs.append(map_to_project_with_technologies(project_model=p, techs=technos))
            return project_with_techs
        
        if collabs:
            project_with_collabs = []
            for p in projects:
                collabs = self.collaborator_dao.find_by_project(project_id=p.pid)
                project_with_collabs.append(map_to_project_with_collaborators(project_model=p, collabs=collabs))
            return project_with_collabs
        
        

        return [map_to_project(p) for p in projects]

    def get_by_pid(
            self, 
            pid: str, 
            techs: bool = False,
            collabs: bool = False
) -> ProjectPublic:
        project = self.project_dao.find_by_id(pid=pid)
        if project is None:
            raise ProjectNotFoundWithPidException(pid)
        
        if techs and collabs:
            collabs = self.collaborator_dao.find_by_project(project_id=project.pid)
            technos = self.technology_dao.find_by_project(project_id=project.pid)
            project_with_collabs_and_techs = map_to_project_with_technologies_and_collaborators(
                    project_model=project,
                    collabs=collabs,
                    techs=technos
            )
            return project_with_collabs_and_techs

        if techs:
            technos = self.technology_dao.find_by_project(project_id=project.pid)
            project_with_techs = map_to_project_with_technologies(project_model=project, techs=technos)
            return project_with_techs
        
        if collabs:
            collabs = self.collaborator_dao.find_by_project(project_id=project.pid)
            project_with_collabs = map_to_project_with_collaborators(project_model=project, collabs=collabs)
            return project_with_collabs

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



