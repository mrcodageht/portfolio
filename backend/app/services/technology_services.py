from fastapi import Depends, HTTPException
from starlette import status
from app.data.dao.technology_dao import TechnologyDao
from app.models.project_model import TechnologyModel
from app.schemas.technology_schema import TechnologyCreate, TechnologyPublic
from app.utils.mapping_utils import map_to_technology_pub


class TechnologyService:
    def __init__(self, technology_dao: TechnologyDao = Depends(TechnologyDao)) -> None:
        self.technology_dao = technology_dao
        
    def get_all(self):
       technos = self.technology_dao.find_all()
       return [map_to_technology_pub(t) for t in technos ]
    
    def get_all_by_project(self, project_id: str):
       technos = self.technology_dao.find_by_project(project_id=project_id)
       return [map_to_technology_pub(t) for t in technos ]
    
    def get_by_id(self, id: str):
        techno = self.technology_dao.find_by_id(id=id)
        if techno is None:
            raise HTTPException(
                detail=f"Techonology not found with the id '{id}'",
                status_code=status.HTTP_404_NOT_FOUND
            )
        
        return map_to_technology_pub(tech_model=techno)

    def save(self, techno_create: TechnologyCreate):
        techno = self.technology_dao.create(item=techno_create)
        return map_to_technology_pub(tech_model=techno)

    def update(self, techno_update: TechnologyCreate, id: str):
        techno = self.technology_dao.update(id=id, item=techno_update)
        return map_to_technology_pub(tech_model=techno)

    def delete(self, id:str):
        self.technology_dao.delete(id=id)



def get_technology_dao():
    return TechnologyDao()
