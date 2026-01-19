from typing import Annotated
from fastapi import APIRouter, Depends, Query, UploadFile, File
from starlette import status as s
from starlette.responses import JSONResponse
from starlette.exceptions import HTTPException
from fastapi.encoders import jsonable_encoder as je

from app.exceptions.global_projects_exceptions import *
from app.schemas.enums import Visibility, Status
from app.schemas.project_schema import ProjectPublic, ProjectBase, ProjectPublicWithTechnologies, ProjectTechnologyCreate, ProjectUpdate
from app.services.project_service import ProjectService
from app.services.services_user import require_admin
from app.schemas.enums import Kind
from app.schemas.project_media_schema import ProjectMediaPublic, ProjectMedia
from app.services.project_media_service import ProjectMediaService

router = APIRouter(prefix="/projects", tags=["project"])

@router.get("", response_model=ProjectPublic)
def get_projects(
        status : Status | None = None,
        visibility : Visibility | None = None,
        collabs: bool | None = None,
        techs: bool | None = None,
        service: ProjectService = Depends(ProjectService)
):
    if techs is None:
        techs = False
    if collabs is None:
        collabs = False
    projects = je(service.get_all( status = status, visibility=visibility, techs=techs, collabs=collabs))
    return JSONResponse(
        content=projects,
        status_code=s.HTTP_200_OK
    )

@router.get("/{pid}", response_model=ProjectPublic)
def get_by_pid(
    pid: str,
    collabs: bool | None = None,
    techs: bool | None = None, 
    service = Depends(ProjectService)
):
    try:
        project = je(service.get_by_pid(pid, techs, collabs))
        return JSONResponse(
            content=project,
            status_code=s.HTTP_200_OK
        )
    except ProjectNotFoundWithPidException as err:
        res = {"details":err.message}
        raise HTTPException(
            detail=err.message,
            status_code=s.HTTP_404_NOT_FOUND
        )

@router.post(
        "", 
        response_model=ProjectPublic,
        dependencies=[Depends(require_admin)]
        )
def create(project : ProjectBase, service = Depends(ProjectService)):
    try:
        project = je(service.save(project_create=project))
        return JSONResponse(
            content=project,
            status_code=s.HTTP_201_CREATED
        )
    except ProjectAlreadyExistsWithSlugException as err:
        res = {"details":err.message}
        raise HTTPException(
            detail=err.message,
            status_code=s.HTTP_409_CONFLICT
        )


@router.put(
        path="/{pid}", 
        response_model=ProjectPublic,
        dependencies=[Depends(require_admin)]
        )
def update(pid: str, project_to_update: ProjectUpdate, service = Depends(ProjectService)):
    project = je(service.update(pid, project_to_update))
    return JSONResponse(
        content=project,
        status_code=s.HTTP_200_OK
    )

@router.delete(
        "/{pid}", 
        status_code=s.HTTP_204_NO_CONTENT,
        dependencies=[Depends(require_admin)]
        )
def delete(pid: str, service = Depends(ProjectService)):
    service.delete(pid)

@router.patch(
        path="/{pid}/technologies",
        status_code=s.HTTP_200_OK,
        response_model=ProjectPublicWithTechnologies,
        dependencies=[Depends(require_admin)]
)
def add_technologies_project(
    pid: str,
    techs: list[ProjectTechnologyCreate],
    services: ProjectService = Depends(ProjectService)
):
    return services.add_technologies_in_project(pid=pid, techs=techs)

@router.delete(
        "/{pid}/technologies/{slug}",
        status_code=s.HTTP_200_OK,
        response_model=ProjectPublicWithTechnologies,
        dependencies=[Depends(require_admin)]
)
def remove_technology_project(
    pid: str,
    slug: str,
    services: ProjectService = Depends(ProjectService)
):
    return services.remove_technology_in_project(
        pid=pid,
        slug=slug
    )

# Section manage media for projects

@router.get("/{pid}/medias", response_model=list[ProjectMediaPublic], status_code=s.HTTP_200_OK)
def get_medias_project(
    pid: str,
    kind: Kind | None = None,
    project_media_service: ProjectMediaService = Depends(ProjectMediaService)
):
    return project_media_service.get_all_by_pid(pid=pid, kind=kind)

@router.post("/{pid}/medias", response_model=ProjectMediaPublic, status_code=s.HTTP_201_CREATED, dependencies=[Depends(require_admin)]
)
async def add_medias_project(
    pid: str,
    media_create: ProjectMedia = Depends(ProjectMedia.as_form),
    file: UploadFile = File(...),
    project_media_service: ProjectMediaService = Depends(ProjectMediaService)
):
    return project_media_service.save(pid=pid, media_create=media_create, file=file)

@router.delete("/medias/{mid}",status_code=s.HTTP_204_NO_CONTENT, dependencies=[Depends(require_admin)]
)
def delete_media_project(
    mid: str,
    project_media_service: ProjectMediaService = Depends(ProjectMediaService)
):
    project_media_service.delete(id=mid)
    

"""
Section manage projects via account git repositories
"""

@router.get("/github/{repo}", status_code=s.HTTP_200_OK)
def get_github_repo(repo: str, service: ProjectService = Depends(ProjectService)):
    return service.get_provider_repo(query=repo, provider="github")

@router.get("/gitlab/{project_name}", status_code=s.HTTP_200_OK)
def get_project_gitlab(project_name: str, service: ProjectService = Depends(ProjectService)):
    """
    Purpose: one
    """
    return service.get_provider_repo(query=project_name, provider="gitlab")
    
# end def

@router.get("/gitlab/contributed_project", status_code=s.HTTP_200_OK)
def get_contributed_projects(service: ProjectService = Depends(ProjectService)):
    """
    Purpose: one
    """

    
# end def


def get_project_service():
    return ProjectService()
