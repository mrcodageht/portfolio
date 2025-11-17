from typing import Any, Optional, List

from app.data.dao.dao_interface import DAOInterface, T
from app.models.project_model import ProjectImageModel


class ProjectImageDao(DAOInterface[ProjectImageModel]):
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