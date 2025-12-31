from typing import Any, Optional, List
import uuid

from fastapi import Depends

from app.data.dao.dao_interface import DAOInterface
from app.data.database import get_db
from sqlalchemy.orm import Session
from app.models.project_model import ProjectMediaModel
from app.data.dao.project_dao import ProjectDao
from starlette import status
from fastapi import HTTPException
from app.schemas.enums import Kind
from app.schemas.project_media_schema import ProjectMediaPublic

class ProjectMediaDao(DAOInterface[ProjectMediaModel]):

    def __init__(self, project_dao: ProjectDao = Depends(ProjectDao) ,db: Session = Depends(get_db)):
        self.db = db
        self.project_dao = project_dao

    def find_all_by_project_id(self, pid: str, kind: Kind | None = None ) -> list[ProjectMediaModel]:
        project = self.project_dao.find_by_id(pid=pid)
        if project is None:
            raise HTTPException(
                detail=f"Project Not found with the pid '{pid}'",
                status_code=status.HTTP_404_NOT_FOUND
            )
    
        if kind is not None:
            print(f"Kind => {kind}")
            medias = self.db.query(ProjectMediaModel).filter_by(project_pid=pid) 
            return medias.filter_by(kind=kind).all()
        
        medias = self.db.query(ProjectMediaModel).filter(ProjectMediaModel.project_pid == pid).all()
        return medias


    def find_all(self) -> list[ProjectMediaModel]:
        pass

    def find_by_id(self, id: str) -> Optional[ProjectMediaModel]:
        pass

    def create(self, item: ProjectMediaPublic, pid: str) -> ProjectMediaModel:
        project = self.project_dao.find_by_id(pid=pid)
        if project is None:
            raise HTTPException(
                detail=f"Project Not found with the pid '{pid}'",
                status_code=status.HTTP_404_NOT_FOUND
            )
        try:
            item.id=str(uuid.uuid4())
            media = ProjectMediaModel(**item.model_dump(exclude_unset=True))
            media.project_pid = pid
            self.db.add(media)
            self.db.commit()
            self.db.refresh(media)
            return media
        except Exception as e:
            print(f"{e}")
            raise HTTPException(
                detail="Media not have been created successfully",
                status_code=status.HTTP_400_BAD_REQUEST
            )
            

    def update(self, id: str, item: ProjectMediaPublic) -> ProjectMediaModel:
        
        media = self.db.query(ProjectMediaModel).filter_by(id=id).first()
        if media is None:
            raise HTTPException(
                detail=f"Media not found with the id {id}",
                status_code=status.HTTP_404_NOT_FOUND
            )
        
        try:
            for f,v in item.model_dump(exclude_unset=True).items():
                if f != "id":
                    setattr(media, f, v)
                print(f"{f} => {v}")
            
            self.db.commit()
            self.db.refresh(media)
            return media
        except Exception as e:
            print(f"{e}")
            raise HTTPException(
                detail="Media not have been created successfully",
                status_code=status.HTTP_400_BAD_REQUEST
            )


    def delete(self, id: str) -> bool:
        pass

    def create_all(self, items):
        raise NotImplementedError

    def update_all(self, ids, items):
        raise NotImplementedError

    def delete_all(self, ids):
        raise NotImplementedError

    def get_total(self) -> int:
        raise NotImplementedError

