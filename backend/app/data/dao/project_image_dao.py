from typing import Any, Optional, List

from fastapi import Depends

from app.data.dao.dao_interface import DAOInterface, T
from app.data.database import get_db
from app.models.project_model import ProjectImageModel
from sqlalchemy.orm import Session

class ProjectImageDao(DAOInterface[ProjectImageModel]):

    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def find_all(self) -> List[ProjectImageModel]:
        pass

    def find_by_id(self, id: Any) -> Optional[ProjectImageModel]:
        pass

    def create(self, item: ProjectImageModel) -> ProjectImageModel:
        pass

    def update(self, id: Any, item: ProjectImageModel) -> Optional[ProjectImageModel]:
        pass

    def delete(self, id: Any) -> bool:
        pass

    def create_all(self, items):
        raise NotImplementedError

    def update_all(self, ids, items):
        raise NotImplementedError

    def delete_all(self, ids):
        raise NotImplementedError

    def get_total(self) -> int:
        raise NotImplementedError

