from starlette import status

from fastapi import Depends, HTTPException

from app.data.dao.collaborator_dao import CollaboratorDao
from app.models.project_model import CollaboratorModel
from app.schemas.collaborator_schema import CollaboratorCreate, CollaboratorPublic
from app.utils.mapping_utils import map_to_collaborator_public


class CollaboratorService:
    def __init__(self, collaborator_dao: CollaboratorDao = Depends(CollaboratorDao)):
        self.collaborator_dao = collaborator_dao
        

    def get_all(self) -> list[CollaboratorPublic]:
        return [map_to_collaborator_public(c) for c in self.collaborator_dao.find_all()]
    
    def get_by_id(self, id:str) -> CollaboratorPublic:
        collaborator = self.collaborator_dao.find_by_id(id=id)
        if collaborator is None:
            raise HTTPException(
                detail=f"Collaborator not found with the id '{id}'",
                status_code=status.HTTP_404_NOT_FOUND
            )
        return map_to_collaborator_public(collaborator)
    
    def save(self, collab_create: CollaboratorCreate) -> CollaboratorPublic:
        collaborator = self.collaborator_dao.create(item=collab_create)
        return map_to_collaborator_public(collab=collaborator)
    
    def update(self, id: str ,collab_update: CollaboratorCreate) -> CollaboratorPublic:
        collaborator = self.collaborator_dao.update(id=id, item=collab_update)
        return map_to_collaborator_public(collaborator)
    
    def delete(self, id: str) -> bool:
        return self.collaborator_dao.delete(id=id)


def get_dao():
    return CollaboratorDao()