from typing import Any, Optional, List

from app.data.dao.dao_interface import DAOInterface, T
from app.models.project_model import TechnologyModel


class TechnologyDao(DAOInterface[TechnologyModel]):
    def find_all(self) -> List[TechnologyModel]:
        pass

    def find_by_id(self, id: Any) -> Optional[TechnologyModel]:
        pass

    def create(self, item: TechnologyModel) -> TechnologyModel:
        pass

    def update(self, id: Any, item: TechnologyModel) -> Optional[TechnologyModel]:
        pass

    def delete(self, id: Any) -> bool:
        pass

    def create_all(self, items):
        raise NotImplementedError

    def update_all(self, ids, items):
        raise NotImplementedError

    def delete_all(self, ids):
        raise NotImplementedError
