
from starlette import status
from fastapi import APIRouter, Depends

from app.schemas.technology_schema import TechnologyCreate, TechnologyPublic
from app.services.technology_services import TechnologyService


router = APIRouter(prefix="/technologies", tags=["Technology"])


@router.get("", status_code=status.HTTP_200_OK, response_model=list[TechnologyPublic])
def get_all(services = Depends(TechnologyService)):
    return services.get_all()

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=TechnologyPublic)
def get_by_id(id: str, services = Depends(TechnologyService)):
    return services.get_by_id(id=id)

@router.post("", status_code=status.HTTP_201_CREATED, response_model=TechnologyPublic)
def create(techno: TechnologyCreate, services = Depends(TechnologyService)):
    return services.save(techno)

@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=TechnologyPublic)
def update(id: str, techno: TechnologyCreate,services = Depends(TechnologyService)):
    return services.update(id=id, techno_update=techno)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: str, services = Depends(TechnologyService)):
   return services.delete(id=id) 

def get_tech_service():
    return TechnologyService()