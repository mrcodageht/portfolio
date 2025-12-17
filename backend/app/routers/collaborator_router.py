from starlette import status

from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException

from app.schemas.collaborator_schema import CollaboratorCreate, CollaboratorPublic
from app.services.collaborateur_service import CollaboratorService


router = APIRouter(
    prefix="/collaborator",
    tags=["Collaborator"])


@router.get("", response_model=list[CollaboratorPublic], status_code=status.HTTP_200_OK)
def get_all(
    services: CollaboratorService = Depends(CollaboratorService)
):
    return services.get_all()
    

@router.get(path="/{id}", response_model=CollaboratorPublic,status_code=status.HTTP_200_OK)
def get_by_id(
    id: str,
    services: CollaboratorService = Depends(CollaboratorService)
):
    return services.get_by_id(id=id)

@router.get("/search", response_model=list[CollaboratorPublic], status_code=status.HTTP_200_OK)
def search(
    firtname: Annotated[str, None] = None,
    lastname: Annotated[str, None] = None,
    role: Annotated[str, None] = None,
    services: CollaboratorService = Depends(CollaboratorService)
):
    pass


@router.post("", response_model=CollaboratorPublic, status_code=status.HTTP_201_CREATED)
def create(
    collab_create: CollaboratorCreate,
    services: CollaboratorService = Depends(CollaboratorService)
):
    return services.save(collab_create=collab_create)

@router.put("/{id}", response_model=CollaboratorPublic, status_code=status.HTTP_200_OK)
def update(
    id: str,
    collab_create: CollaboratorCreate,
    services: CollaboratorService = Depends(CollaboratorService)
):
    return services.update(id=id, collab_update=collab_create)
    

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(
    id: str,
    services: CollaboratorService = Depends(CollaboratorService)
):
    if services.delete(id=id) is not True:
        raise HTTPException(
            detail=f"Erreur lors de la suppression",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )



