from fastapi import Depends
from app.data.dao.collaborator_dao import CollaboratorDao
from app.data.dao.project_dao import ProjectDao
from app.data.dao.technology_dao import TechnologyDao
from app.schemas.stats_schema import Stats


class RessourceService:
    def __init__(
            self,
            project_dao: ProjectDao = Depends(ProjectDao),
            collaborator_dao: CollaboratorDao = Depends(CollaboratorDao),
            technology_dao: TechnologyDao = Depends(TechnologyDao)
        ) -> None:
        self.project_dao = project_dao
        self.collaborator_dao = collaborator_dao
        self.technology_dao = technology_dao

    def get_stats(self):
        nb_tech = self.technology_dao.get_total()
        nb_project = self.project_dao.get_total()
        nb_collab = self.collaborator_dao.get_total()
        stats : Stats = Stats(
            technologies=nb_tech,
            collaborators=nb_collab,
            projects=nb_project
        )
        return stats