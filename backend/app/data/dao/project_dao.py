from abc import ABC
from typing import Any, Optional, List

from app.data.dao.dao_interface import DAOInterface, T
from app.models.project_model import ProjectModel
from app.schemas.project_schema import Project


class ProjectDao(DAOInterface[ProjectModel]):
    def find_all(self) -> List[ProjectModel]:
        pass

    def find_by_id(self, id: Any) -> Optional[ProjectModel]:
        pass

    def create(self, item: ProjectModel) -> ProjectModel:
        pass

    def update(self, id: Any, item: ProjectModel) -> Optional[ProjectModel]:
        pass

    def delete(self, id: Any) -> bool:
        pass