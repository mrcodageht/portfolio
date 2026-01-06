from typing import Any, Optional, List
from starlette import status
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.data.dao.dao_interface import DAOInterface, T
from app.models.project_model import ProjectModel, TechnologyModel
from app.data.database import get_db
from app.schemas.technology_schema import TechnologyCreate


class TechnologyDao(DAOInterface[TechnologyModel]):

    def __init__(self, db: Session = Depends(get_db)):
        self.db = db
        super().__init__()

    def find_all(self) -> List[TechnologyModel]:
        technos = self.db.query(TechnologyModel).all()
        return technos

    def find_by_id(self, id: str) -> Optional[TechnologyModel]:
        techno = self.db.query(TechnologyModel).filter(TechnologyModel.id==id).first()
        return techno
    
    def find_by_slug(self, slug: str) -> Optional[TechnologyModel]:
        techno = self.db.query(TechnologyModel).filter(TechnologyModel.slug==slug).first()
        return techno
    
    def find_by_project(self, project_id) -> list[TechnologyModel]:
        techs = self.db.query(TechnologyModel).join(TechnologyModel.projects).filter(ProjectModel.pid == project_id).all()
       
        return techs

    def create(self, item: TechnologyCreate) -> TechnologyModel:
        techno: ProjectModel = TechnologyModel(**item.model_dump(exclude_unset=True))

        techno.slug = item.name.lower().replace(" ","-")
        
        is_exists = self.db.query(TechnologyModel).filter(TechnologyModel.slug==techno.slug).first()
        if is_exists is not None:
            raise HTTPException(
                detail=f"Technology '{techno.slug}' already exists",
                status_code=status.HTTP_409_CONFLICT
            )

        try:
            self.db.add(techno)
            self.db.commit()
            self.db.refresh(techno) 
            return techno
        except Exception as e:
            self.db.rollback()
            print(f"Erreur lors de la sauvegarde {e}")
            raise HTTPException(
                detail="Erreur lors de la sauvegarde.",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def update(self, id: str, item: TechnologyCreate) -> Optional[TechnologyModel]:
        techno = self.find_by_id(id=id)
        if techno is None:
            raise HTTPException(
                detail=f"Techonology not found with the id '{id}'",
                status_code=status.HTTP_404_NOT_FOUND
            )
        
        slug = item.name.lower().replace(" ","-")
        
        if slug != techno.slug:
            techno.slug = slug

            is_exists = self.db.query(TechnologyModel).filter(TechnologyModel.slug==techno.slug).first()
            if is_exists is not None:
                raise HTTPException(
                    detail=f"Technology '{techno.slug}' already exists",
                    status_code=status.HTTP_409_CONFLICT
                )
        
        for f,v in item.model_dump(exclude_unset=True).items():
            setattr(techno,f,v)
        try:
            self.db.commit()
            self.db.refresh(techno)
            return techno
        except Exception as e:
            self.db.rollback()
            print(f"Erreur lors de la sauvegarde {e}")
            raise HTTPException(
                detail="Erreur lors de la sauvegarde.",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
                 

    def delete(self, id: str) -> bool:
        techno = self.find_by_id(id=id)
        if techno is None:
            raise HTTPException(
                detail=f"Techonology not found with the id '{id}'",
                status_code=status.HTTP_404_NOT_FOUND
            )

        try:
            self.db.delete(techno)
            self.db.commit()
            return True
        except Exception as e:
            self.db.rollback()
            print(f"Erreur lors de la sauvegarde {e}")
            raise HTTPException(
                detail="Erreur lors de la sauvegarde.",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


    def create_all(self, items):
        raise NotImplementedError

    def update_all(self, ids, items):
        raise NotImplementedError

    def delete_all(self, ids):
        raise NotImplementedError

    def get_total(self) -> int:
        return self.db.query(TechnologyModel).count()

