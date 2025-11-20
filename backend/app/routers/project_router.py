from fastapi import APIRouter, HTTPException, Depends
from starlette import status
from starlette.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from app.services.project_service import ProjectService

router = APIRouter(prefix="/projects", tags=["projects"])

@router.get("", response_model=None)
def get_projects(service: ProjectService = Depends(ProjectService)):
    projects = jsonable_encoder(service.get_all())
    return JSONResponse(
        content=projects,
        status_code=status.HTTP_200_OK
    )

@router.get("/{pid}")
def get_by_id(pid: str):
    return None

@router.post("")
def create():
    return None

@router.put("")
def update():
    return None

@router.delete("")
def delete():
    return None

def get_project_service():
    return ProjectService()