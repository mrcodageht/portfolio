from typing import Any, Optional, List

from click import option
from fastapi import Depends, HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session, joinedload
from starlette import status as s

from app.data.dao.dao_interface import DAOInterface, T
from app.data.database import get_db
from app.models.project_model import ProjectImageModel, ProjectModel, TechnologyModel
from app.schemas.enums import Status, Visibility
from app.schemas.project_schema import ProjectBase, ProjectTechnologyCreate, ProjectUpdate



class ProjectDao:

    def __init__(self, db : Session = Depends(get_db)):
        self.db = db

    def find_all(
            self,
            status : Status | None = None,
            visibility : Visibility | None = None
    ) -> list[ProjectModel]:

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


    def update(self, id: str, item: ProjectUpdate) -> Optional[type[ProjectModel]]:
        project_existing = self.find_by_id(pid=id)
        if project_existing is None:
            raise HTTPException(
                detail=f"Project not found with the pid '{id}'",
                status_code=s.HTTP_404_NOT_FOUND
            )

        for f,v in item.model_dump(exclude_unset=True).items():
            setattr(project_existing,f,v)          
        try:
            self.db.commit()
            self.db.refresh(project_existing)
            return project_existing
        except Exception as ex:
            print(f"xx> Error : {ex}")

    def delete(self, id: str) -> bool:
        project_existing = self.find_by_id(pid=id)
        if project_existing is None:
            raise HTTPException(
                detail=f"Project not found with the pid '{id}'",
                status_code=s.HTTP_404_NOT_FOUND
            )
        try:
            images = self.db.query(ProjectImageModel).filter(ProjectImageModel.project_pid==id).all()
            for im in images:
                self.db.delete(im)
            self.db.delete(project_existing)
            self.db.commit()
            return True
        except Exception as ex:
            print(f"Error : {ex}")
            raise HTTPException(
                detail=f"Failed to delete the project with the pid '{id}'",
                status_code=s.HTTP_400_BAD_REQUEST
            )
        
    def add_technologies(self, pid: str ,techs: list[TechnologyModel]) -> ProjectModel:
        project_existing = self.db.query(ProjectModel).join(ProjectModel.technologies).filter(ProjectModel.pid==pid).first()
        if project_existing is None:
            raise HTTPException(
                detail=f"Project not found with the pid '{id}'",
                status_code=s.HTTP_404_NOT_FOUND
            )
        
        try:
            for t in techs:
                project_existing.technologies.append(t)
            self.db.commit()
            self.db.refresh(project_existing)
            return project_existing
        except Exception as e:
            print(f"Error => {e}")
            raise HTTPException(
                detail="Failed to update the project",
                status_code=s.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def remove_technologies(self, pid: str, tech: TechnologyModel):
        project_existing = self.db.query(ProjectModel).join(ProjectModel.technologies).filter(ProjectModel.pid==pid).first()
        if project_existing is None:
            raise HTTPException(
                detail=f"Project not found with the pid '{id}'",
                status_code=s.HTTP_404_NOT_FOUND
            )
        
        tech_existing = False
        for t in project_existing.technologies:
            if t.id==tech.id:
                tech_existing = True
        if tech_existing:
            try:
                project_existing.technologies.remove(tech)
            
                self.db.commit()
                self.db.refresh(project_existing)
                return project_existing
            except Exception as e:
                print(f"Error => {e}")
                raise HTTPException(
                    detail="Failed to update the project",
                    status_code=s.HTTP_500_INTERNAL_SERVER_ERROR
                )

        raise HTTPException(
            detail=f"Technology with the slug '{tech.slug}' not exists in this project",
            status_code=s.HTTP_404_NOT_FOUND
        )
        
    def get_total(self)-> int:
        count = self.db.query(ProjectModel).count()
        return count


    def create_all(self, items: List[ProjectBase]):
        raise NotImplementedError

    def update_all(self, ids, items):
        raise NotImplementedError

    def delete_all(self, ids: List[int]):
        raise NotImplementedError
