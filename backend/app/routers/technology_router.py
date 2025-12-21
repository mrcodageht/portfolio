
from starlette import status
from fastapi import APIRouter, Depends

from app.schemas.technology_schema import TechnologyCreate, TechnologyPublic
from app.services.technology_services import TechnologyService
from app.services.services_user import require_admin


router = APIRouter(prefix="/technologies", tags=["Technology"])


@router.get("", status_code=status.HTTP_200_OK, response_model=list[TechnologyPublic])
def get_all(project_id: str | None = None, services: TechnologyService = Depends(TechnologyService)):
    if project_id is not None:
        return services.get_all_by_project(project_id=project_id)
    return services.get_all()

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=TechnologyPublic)
def get_by_id(id: str, services: TechnologyService = Depends(TechnologyService)):
    return services.get_by_id(id=id)

@router.post(
        "", 
        status_code=status.HTTP_201_CREATED, 
        response_model=TechnologyPublic,
        dependencies=[Depends(require_admin)]
    )
def create(techno: TechnologyCreate, services: TechnologyService = Depends(TechnologyService)):
    return services.save(techno)

@router.put(
        "/{id}", 
        status_code=status.HTTP_200_OK, 
        response_model=TechnologyPublic,
        dependencies=[Depends(require_admin)]
        )
def update(id: str, techno: TechnologyCreate,services: TechnologyService = Depends(TechnologyService)):
    return services.update(id=id, techno_update=techno)

@router.delete(
        "/{id}", 
        status_code=status.HTTP_204_NO_CONTENT,
        dependencies=[Depends(require_admin)]
        )
def delete(id: str, services: TechnologyService = Depends(TechnologyService)):
   return services.delete(id=id) 

def get_tech_service():
    return TechnologyService()