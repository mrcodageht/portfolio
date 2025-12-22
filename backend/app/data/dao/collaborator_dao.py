from typing import Any, Optional, List

from fastapi import Depends, HTTPException

from sqlalchemy.orm import Session, joinedload
from starlette import status

from app.data.dao.dao_interface import DAOInterface, T
from app.data.database import get_db
from app.models.project_model import CollaboratorModel, ProjectModel
from app.schemas.collaborator_schema import CollaboratorCreate


class CollaboratorDao(DAOInterface[CollaboratorModel]):
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db
        super().__init__()


    def find_all(self) -> List[CollaboratorModel]:
        return self.db.query(CollaboratorModel).all()

    def find_by_id(self, id: str) -> Optional[CollaboratorModel]:
        return self.db.query(CollaboratorModel).filter(CollaboratorModel.id==id).first()

    def find_by_project(self, project_id)-> list[CollaboratorModel]:
        collabs = self.db.query(CollaboratorModel).join(CollaboratorModel.projects).filter(ProjectModel.pid==project_id).all()
        return collabs

    def create(self, item: CollaboratorCreate) -> CollaboratorModel:
        collab = CollaboratorModel(**item.model_dump(exclude_unset=True))
        try:
            self.db.add(collab)
            self.db.commit()
            self.db.refresh(collab)
            return collab
        except Exception as e:
            self.db.rollback()
            print(f"Erreur : {e}")

            raise HTTPException(
                detail="Error",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def update(self, id: str, item: CollaboratorCreate) -> Optional[CollaboratorModel]:
        is_exists = self.find_by_id(id=id)

        if is_exists is None:
            raise HTTPException(
                detail=f"Collaborator not found with id '{id}'",
                status_code=status.HTTP_404_NOT_FOUND
            )
        
        for f,v in item.model_dump(exclude_unset=True).items():
            setattr(is_exists, f, v)
        
        try:
            self.db.commit()
            self.db.refresh(is_exists)
            return is_exists
        except Exception as e:
            self.db.rollback()
            print(f"Erreur : {e}")
            raise HTTPException(
                detail="Error",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


    def delete(self, id: str) -> bool:
        is_exists = self.find_by_id(id=id)

        if is_exists is None:
            raise HTTPException(
                detail=f"Collaborator not found with id '{id}'",
                status_code=status.HTTP_404_NOT_FOUND
            )
        
        try:
            self.db.delete(is_exists)
            self.db.commit()
            return True
        except Exception as e:
            self.db.rollback()
            print(f"Erreur : {e}")
            raise HTTPException(
                detail="Error",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        


    def create_all(self, items):
        raise NotImplementedError

    def update_all(self, ids, items):
        raise NotImplementedError

    def delete_all(self, ids):
        raise NotImplementedError
