from starlette import status

from typing import Annotated
from fastapi import APIRouter

from app.schemas.collaborator_schema import CollaboratorCreate, CollaboratorPublic


router = APIRouter(
    prefix="/collaborator",
    tags=["Collaborator"])


@router.get("", response_model=list[CollaboratorPublic], status_code=status.HTTP_200_OK)
def get_all():
    pass

@router.get(path="/{id}", response_model=CollaboratorPublic,status_code=status.HTTP_200_OK)
def get_by_id():
    pass

@router.get("/search", response_model=list[CollaboratorPublic], status_code=status.HTTP_200_OK)
def search(
    firtname: Annotated[str, None] = None,
    lastname: Annotated[str, None] = None,
    role: Annotated[str, None] = None,

):
    pass


@router.post("", response_model=CollaboratorPublic, status_code=status.HTTP_201_CREATED)
def create(
    collab_create: CollaboratorCreate
):
    pass

@router.put("/{id}", response_model=list[CollaboratorPublic], status_code=status.HTTP_200_OK)
def update(
    id: str,
    collab_create: CollaboratorCreate
):
    pass
    

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(
    id: str
):
    pass


