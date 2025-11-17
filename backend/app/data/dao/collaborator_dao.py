from typing import Any, Optional, List

from app.data.dao.dao_interface import DAOInterface, T
from app.models.project_model import CollaboratorModel
from app.schemas.collaborator_schema import Collaborator
from app.schemas.project_schema import Project


class CollaboratorDao(DAOInterface[CollaboratorModel]):
    def find_all(self) -> List[CollaboratorModel]:
        pass

    def find_by_id(self, id: Any) -> Optional[CollaboratorModel]:
        pass

    def create(self, item: Collaborator) -> CollaboratorModel:
        pass

    def update(self, id: Any, item: CollaboratorModel) -> Optional[CollaboratorModel]:
        pass

    def delete(self, id: Any) -> bool:
        pass