from typing import Any, Optional, List

from click import option
from fastapi import Depends
from sqlalchemy import func
from sqlalchemy.orm import Session, joinedload

from app.data.dao.dao_interface import DAOInterface, T
from app.data.database import get_db
from app.models.project_model import ProjectModel
from app.schemas.enums import Status, Visibility
from app.schemas.project_schema import ProjectBase


class ProjectDao(DAOInterface[ProjectModel]):

    def __init__(self, db : Session = Depends(get_db)):
        self.db = db

    def find_all(
            self,
            status : Status | None = None,
            visibility : Visibility | None = None
    ) -> list[type[ProjectModel]]:

        if status is not None and visibility is not None :
            return self.db.query(ProjectModel).filter_by(
                status=status,
                visibility=visibility
            ).all()

        if status is not None:
            return self.db.query(ProjectModel).filter_by(status=status).all()

        if visibility is not None:
            return self.db.query(ProjectModel).filter_by(visibility=visibility).all()

        return self.db.query(ProjectModel).all()



    def find_by_id(self, pid: str) -> type[ProjectModel]:
        project = (self.db.query(ProjectModel)
            .filter_by(pid=pid).first())
        return project
    
    def find_by_slug(self, slug:str)-> ProjectModel:
        project = (self.db.query(ProjectModel).filter(func.lower(ProjectModel.slug)==func.lower(slug)).first())
        return project

    def create(self, project: ProjectBase) -> ProjectModel:
        try:
            db_project = ProjectModel(**project.model_dump(exclude_unset=True))
            self.db.add(db_project)
            self.db.commit()
            self.db.refresh(db_project)
            return db_project
        except Exception as ex:
            self.db.rollback()
            print(f"Error : {ex}")
            raise Exception("the project not have been created successfully.")


    def update(self, id: Any, item: ProjectModel) -> Optional[ProjectModel]:
        pass

    def delete(self, id: Any) -> bool:
        pass