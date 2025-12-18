from fastapi import APIRouter, Depends, Query
from starlette import status as s
from starlette.responses import JSONResponse
from starlette.exceptions import HTTPException
from fastapi.encoders import jsonable_encoder as je

from app.exceptions.global_projects_exceptions import *
from app.schemas.enums import Visibility, Status
from app.schemas.project_schema import ProjectPublic, ProjectBase, ProjectUpdate
from app.services.project_service import ProjectService
from app.services.services_user import require_admin

router = APIRouter(prefix="/projects", tags=["projects"])

@router.get("", response_model=list[ProjectPublic])
def get_projects(
        status : Status | None = None,
        visibility : Visibility | None = None,
        service: ProjectService = Depends(ProjectService)
):
    print(f"status demande : {status}")

    projects = je(service.get_all( status = status, visibility=visibility))
    return JSONResponse(
        content=projects,
        status_code=s.HTTP_200_OK
    )

@router.get("/{pid}", response_model=ProjectPublic)
def get_by_pid(pid: str, service = Depends(ProjectService)):
    try:
        project = je(service.get_by_pid(pid))
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
            status_code=s.HTTP_400_BAD_REQUEST
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

def get_project_service():
    return ProjectService()