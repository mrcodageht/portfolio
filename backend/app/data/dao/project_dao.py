from typing import Any, Optional, List

from fastapi import Depends
from sqlalchemy.orm import Session, joinedload

from app.data.dao.dao_interface import DAOInterface, T
from app.data.database import get_db
from app.models.project_model import ProjectModel


class ProjectDao(DAOInterface[ProjectModel]):

    def __init__(self, db : Session = Depends(get_db)):
        self.db = db

    def find_all(self) -> list[type[ProjectModel]]:
        return (self.db.query(ProjectModel)
                .options(
            joinedload(ProjectModel.images),
            joinedload(ProjectModel.collaborators),
            joinedload(ProjectModel.technologies)
                ).all()
        )


    def find_by_id(self, id: Any) -> Optional[ProjectModel]:
        pass

    def create(self, item: ProjectModel) -> ProjectModel:
        pass

    def update(self, id: Any, item: ProjectModel) -> Optional[ProjectModel]:
        pass

    def delete(self, id: Any) -> bool:
        pass